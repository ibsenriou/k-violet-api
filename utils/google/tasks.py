import importlib
from threading import Thread
from django.urls import URLResolver
from functools import wraps
import json
from google.cloud import tasks_v2
from django.conf import settings
from django.urls import reverse
import requests

client = None


class UrlNames:
    url_list = None

    def get(self, f) -> list:
        if self.url_list is None:
            self.url_list = self.get_url_names()
        for app_name, urls in self.url_list:
            for url in urls:
                if isinstance(url, URLResolver):
                    for key in url.reverse_dict.keys():
                        # check if key is instance of a function
                        if not isinstance(key, str):
                            if key.__name__ == f.__qualname__.split('.')[0]:
                                return reverse(f'{app_name}:{key.initkwargs["basename"]}-list')
        raise Exception(f'Function {f.__qualname__} not found in any url')

    def get_url_names(self):
        from django.apps import apps

        list_of_all_urls = list()
        for name, app in apps.app_configs.items():
            mod_to_import = f'src.{name}.urls'
            try:
                url_module = importlib.import_module(
                    mod_to_import)
                urls = getattr(url_module, "urlpatterns")
                app_name = getattr(url_module, "app_name")
                list_of_all_urls.append([app_name, urls])
            except ImportError as ex:
                pass

        return list_of_all_urls


url_names = UrlNames()


def resolve_url(host: str, url: str):
    if host.endswith('/'):
        host = host[:-1]
    if url.startswith('/'):
        url = url[1:]
    return f'{host}/{url}'


def execute_task(queue: str, f):
    def wrapper(payload: dict, delay: int = 0, request=None, **kwargs):
        url = url_names.get(f)
        if settings.CLOUDRUN_SERVICE_URL is not None:
            url = resolve_url(settings.CLOUDRUN_SERVICE_URL, url)
        else:
            url = resolve_url(settings.LOCALHOST_URL, url)
        task = Task(payload, url, delay, queue, request=request)
        return task.execute(**kwargs)
    return wrapper


def task(queue: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        setattr(wrapper, 'task', execute_task(queue, f))
        return wrapper

    return decorator


class Task:
    payload: dict
    delay: int
    queue: str
    parent: str
    project: str = settings.GOOGLE_CLOUD_PROJECT
    location: str = settings.GOOGLE_CLOUD_LOCATION
    id: str = None
    url: str
    request = None

    def __init__(self, payload: dict, url: str, delay: int = 0, queue: str = 'default', id: str = None, request=None):
        self.payload = payload
        self.delay = delay
        self.queue = queue
        self.id = id
        self.url = url
        self.request = request

    def execute(self):
        global client
        headers = {
            "Content-type": "application/json"
        }

        if (self.request is not None):
            headers['cookie'] = self.request.headers['cookie']

        if settings.CLOUDRUN_SERVICE_URL is not None:
            if client is None:
                client = tasks_v2.CloudTasksClient()
            task = tasks_v2.Task(
                http_request=tasks_v2.HttpRequest(
                    http_method=tasks_v2.HttpMethod.POST,
                    url=self.url,
                    headers=headers,
                    body=json.dumps(self.payload).encode(),
                ),
                name=(
                    client.task_path(self.project, self.location,
                                     self.queue, self.id)
                    if self.id is not None
                    else None
                ),
            )
            return client.create_task(
                tasks_v2.CreateTaskRequest(
                    parent=client.queue_path(
                        self.project, self.location, self.queue),
                    task=task,
                )
            )
        else:
            def process_task_request(url, payload, headers):
                requests.post(url, json=payload, headers=headers)

            thread = Thread(target=process_task_request, args=(
                self.url, self.payload, headers))
            thread.start()
