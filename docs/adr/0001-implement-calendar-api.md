# ADR 001: Event-Driven Calendar System with Dynamic Event Types

## Context

In the development of the condominium management system, we need a flexible and extensible way to manage calendar events that vary by type (e.g., meetings, repairs, moving). The calendar system needs to handle multiple event types, each with its own specific fields and behaviors, but also share a common base structure for basic event properties.

The event types are dynamic, and we need a solution that allows for adding new event types without extensive changes to the system, providing scalability for future requirements.

## Decision

We will implement a model and serializer-based approach that dynamically selects the correct model and serializer based on the `event_type` field in the request data.

### Key Components:

1. **Event Type Mapping**: We will use a dictionary to map event types (e.g., `meetingcalendarevent`, `repaircalendarevent`, `movingcalendarevent`) to their respective model classes and serializers.
2. **Model Structure**: 
   - A base model, `CondominiumBaseCalendarEvent`, will handle common fields such as `title`, `description`, `start`, `end`, and `allDay`.
   - Event-specific subclasses, such as `MeetingCalendarEvent`, `RepairCalendarEvent`, and `MovingCalendarEvent`, will extend the base model and can include their own additional fields as needed.
3. **Serializer Structure**: 
   - A base serializer, `CondominiumBaseCalendarEventSerializer`, will handle serialization of common fields.
   - Subclass-specific serializers will inherit from the base serializer and extend it with additional fields unique to each event type.
4. **Dynamic Event Type Handling**:
   - In the viewset, the event type is extracted from the request and used to determine the appropriate model and serializer for the event.
   - The correct serializer is dynamically instantiated, validated, and saved, ensuring that the event data is correctly handled according to its type.

### Example Flow:

- A request to create a new calendar event includes an `event_type` field (e.g., `meetingcalendarevent`).
- The viewset uses this type to lookup the appropriate model and serializer.
- The serializer validates the data and saves the event to the database.
- A response is returned with the serialized data for the newly created event.

### Detailed Implementation

#### Models:

```python
from django.db import models
from django.contrib.contenttypes.models import ContentType
from src.core.models import HomespaceTenentBaseModel

class CondominiumBaseCalendarEvent(HomespaceTenentBaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    allDay = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.content_type:
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        super().save(*args, **kwargs)

class MeetingCalendarEvent(CondominiumBaseCalendarEvent):
    # Add specific fields for the Meeting event as needed
    pass

class RepairCalendarEvent(CondominiumBaseCalendarEvent):
    # Add specific fields for the Repair event as needed
    pass

class MovingCalendarEvent(CondominiumBaseCalendarEvent):
    # Add specific fields for the Moving event as needed
    pass

```

#### Serializers:

```python
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from src.condominium.models import CondominiumBaseCalendarEvent, MeetingCalendarEvent, RepairCalendarEvent
from src.condominium.models.model_condominium_calendar_event import MovingCalendarEvent

class BaseCalendarEventSerializer(serializers.ModelSerializer):
    """
    Base serializer for all event subtypes
    """
    title = serializers.CharField(write_only=True)
    description = serializers.CharField(write_only=True, required=False, allow_blank=True)
    allDay = serializers.BooleanField(write_only=True, required=False, default=False)
    start = serializers.DateTimeField(write_only=True)
    end = serializers.DateTimeField(write_only=True)

    class Meta:
        model = CondominiumBaseCalendarEvent
        fields = ['title', 'description', 'allDay', 'start', 'end']

class MeetingCalendarEventSerializer(BaseCalendarEventSerializer):
    class Meta:
        model = MeetingCalendarEvent
        fields = BaseCalendarEventSerializer.Meta.fields

class RepairCalendarEventSerializer(BaseCalendarEventSerializer):
    class Meta:
        model = RepairCalendarEvent
        fields = BaseCalendarEventSerializer.Meta.fields

class MovingCalendarEventSerializer(BaseCalendarEventSerializer):
    class Meta:
        model = MovingCalendarEvent
        fields = BaseCalendarEventSerializer.Meta.fields

```

#### Viewset:

```python
import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from ..models import CondominiumBaseCalendarEvent, MeetingCalendarEvent, RepairCalendarEvent
from ..models.model_condominium_calendar_event import MovingCalendarEvent
from ..serializers.serializer_condominium_calendar_event import CondominiumBaseCalendarEventSerializer, \
    MeetingCalendarEventSerializer, RepairCalendarEventSerializer, MovingCalendarEventSerializer

# Define a mapping of event types to model classes and serializers
EVENT_TYPE_MODEL_MAPPING = {
    'meetingcalendarevent': (MeetingCalendarEvent, MeetingCalendarEventSerializer),
    'repaircalendarevent': (RepairCalendarEvent, RepairCalendarEventSerializer),
    'movingcalendarevent': (MovingCalendarEvent, MovingCalendarEventSerializer),
}

class CondominiumCalendarEventModelViewSet(viewsets.ModelViewSet):
    queryset = CondominiumBaseCalendarEvent.objects.all().order_by('-created_at')
    serializer_class = CondominiumBaseCalendarEventSerializer

    def create(self, request, *args, **kwargs):
        event_type = request.data.get('event_type')

        if not event_type or event_type.lower() not in EVENT_TYPE_MODEL_MAPPING:
            raise ValidationError({"detail": "Invalid or missing event type"})

        # Get the model and serializer for the event type
        model_class, serializer_class = EVENT_TYPE_MODEL_MAPPING[event_type.lower()]

        serializer = serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        response_serializer = self.get_serializer(instance)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        event_type = request.data.get('event_type')
        logging.warning(f"Event type received: {event_type}")

        if not event_type or event_type.lower() not in EVENT_TYPE_MODEL_MAPPING:
            raise ValidationError({"detail": "Invalid or missing event type"})

        model_class, serializer = EVENT_TYPE_MODEL_MAPPING[event_type.lower()]

        instance = self.get_object()

        serializer = serializer(instance, data=request.data, context={'request': request}, partial=True)

        serializer.is_valid(raise_exception=True)

        instance = serializer.save()

        response_serializer = self.get_serializer(instance)

        return Response(response_serializer.data, status=status.HTTP_200_OK)

```

### Consequences
#### Flexibility: This approach allows the system to easily add new event types by creating new models and serializers without changing the underlying infrastructure.
#### Extensibility: As new event types are added, only minimal code changes are necessary, mainly to update the mapping and add corresponding models and serializers.
#### Complexity: While this solution introduces dynamic behavior, it is simple to maintain and extend by adhering to well-defined mappings and serializers.
