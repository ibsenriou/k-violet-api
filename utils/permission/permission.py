from rest_framework import status
from rest_framework.response import Response

import functools
import re

def _check_permission(permission_and_action, resolved_permissions, attributes):
    if attributes is None:
        attributes = {}

    component_permission, action = permission_and_action.split(':')
    component_permission_path = component_permission.split('.')
    matched_attributes = []
    has_permission = False

    for i in range(len(component_permission_path)):
        sliced_path = '.'.join(component_permission_path[:i + 1])
        for resolved_permission_and_action in resolved_permissions:
            local_matched_attributes = []
            filters = re.findall(r'\[([^\]]*)\]', resolved_permission_and_action)
            if filters:
                attributes_match = True
                for filter in filters:
                    key, value = filter.split('=') if '=' in filter else (filter, None)
                    if key not in attributes or attributes[key] != value:
                        attributes_match = False
                        break
                    else:
                        local_matched_attributes.append(filter)
                if not attributes_match:
                    continue

            resolved_permission, resolved_action = resolved_permission_and_action.split(':')
            resolved_action_without_filters = re.sub(r'\[[^\]]*\]', '', resolved_action)
            resolved_permission_without_filters = re.sub(r'\[[^\]]*\]', '', resolved_permission)
            if resolved_permission_without_filters.startswith(sliced_path):
                sliced_resolved_permission = resolved_permission_without_filters.replace(sliced_path, '')
                if sliced_resolved_permission == '.*' or i == len(component_permission_path) - 1 and sliced_resolved_permission == '':
                    if resolved_action_without_filters == '*' or resolved_action_without_filters == action:
                        matched_attributes.append(local_matched_attributes)
                        has_permission = True

    return has_permission, matched_attributes


def check_permission(permission, permission_attributes: callable = lambda a,*b,**c: {}, debug=False):
    """
    Decorator that checks if the user has the required permission to access the view.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            resolved_permissions = request.session.get('resolved_permissions', [])
            has_permission, attri = _check_permission(permission, resolved_permissions, permission_attributes(request, *args, **kwargs))
            if not debug and not has_permission:
                return Response(status=status.HTTP_403_FORBIDDEN,
                                data={'detail': 'You do not have permission to perform this action.'})
            kwargs["permission_attributes"] = attri
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
