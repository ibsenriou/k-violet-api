from rest_framework import serializers
from rest_framework.fields import SkipField

from collections import OrderedDict


class NestedDescriptionField(serializers.Field):
    """Nested description field."""

    def __init__(self, fk_field_name=None, *args, **kwargs):
        """Init method."""
        self.fk_field_name = fk_field_name
        kwargs["required"] = False
        super(NestedDescriptionField, self).__init__(*args, **kwargs)

    def to_representation(self, value, instance):
        """Return nested description."""
        fk_path = self.fk_field_name.split(".")
        instance_fk = instance
        for fk in fk_path:
            instance_fk = getattr(instance_fk, fk)

        return str(instance_fk if instance_fk is not None else "")


class NestedDetailsModelSerializer(serializers.ModelSerializer):
    """Nested model serializer."""

    def to_representation(self, instance):
        ret = OrderedDict()
        fields = [field for field in self._readable_fields]

        for field in fields:
            if "fk_" in field.field_name:
                field_name = field.field_name.replace("fk_", "")
                nested_field = NestedDescriptionField(field.field_name)
                nested_field.bind(field_name, self)
                fields.append(nested_field)

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                pass
            if isinstance(field, NestedDescriptionField):
                ret[field.field_name] = field.to_representation(attribute, instance)
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret
