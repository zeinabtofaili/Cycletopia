from .models import UsedBike
from rest_framework import serializers

class UsedBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedBike
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "address",
            "description",
            "grouping",
            "size",
            "color",
            "price",
            "sellerPhoneNumber",
            "sold",
            "sellerEmail",
            "image",
            "get_image",
            "get_thumbnail",
            "user"
        )