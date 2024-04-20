from .models import DonatedBike
from rest_framework import serializers

class DonatedBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatedBike
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "address",
            "donatorPhoneNumber",
            "donatorEmail",
            "image",
            "get_image",
            "get_thumbnail",
            "user"
        )