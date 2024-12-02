from django.db import models


class CustomUniqueModelManager(models.Manager):
    def __init__(self, *args, createResolveFunction=None) -> None:
        self.createResolveFunction = createResolveFunction
        self.unique_fields = args
        super().__init__()

    def create(self, **obj_data):
        dict_unique_fields = {}
        for field in self.unique_fields:
            if field in obj_data:
                dict_unique_fields[field] = obj_data[field]
            else:
                dict_unique_fields[field] = None

        dict_default_fields = {}
        for field in obj_data:
            if field not in self.unique_fields:
                dict_default_fields[field] = obj_data[field]

        object, created = self.get_or_create(
            **dict_unique_fields,
            defaults=dict_default_fields
        )
        if not created:
            dict_update_fields = dict_default_fields

            if self.createResolveFunction:
                dict_update_fields = dict_update_fields | \
                    self.createResolveFunction()

            for field in dict_update_fields:
                setattr(object, field, dict_update_fields[field])

            object.save()
        return object
