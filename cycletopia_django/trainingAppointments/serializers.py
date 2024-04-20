from .models import TrainingAppointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingAppointment
        fields = (
            "id",
            "phone",
            "email",
            "user",
            "time",
            "date",
            "bike_type"
        )