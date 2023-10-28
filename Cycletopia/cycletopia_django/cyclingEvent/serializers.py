from .models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "map_url",
            "get_image",
            "attendees",
            "date_and_time"
        )
