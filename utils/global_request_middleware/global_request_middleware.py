import threading

class EmptyRequest:
    user = None

class GlobalRequestMiddleware:
    _threadmap = {}

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self._threadmap[threading.get_ident()] = request
        response = self.get_response(request)
        try:
            del self._threadmap[threading.get_ident()]
        except KeyError:
            pass
        return response

    @classmethod
    def get_current_request(cls):
        return cls._threadmap.get(threading.get_ident(), EmptyRequest())
