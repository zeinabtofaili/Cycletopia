from rest_framework import serializers
from .models import RentalProduct
class RentPriceSerializerField(serializers.Field):
    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):
        return data

class RentalProductSerializer(serializers.ModelSerializer):
    rent_duration_and_price = RentPriceSerializerField()

    class Meta:
        model = RentalProduct
        fields = (
            'id', 
            'name', 
            'description',
            'get_absolute_url',
            'rent_duration_and_price',
            'user',
            'get_image',
            'get_thumbnail',
            'grouping',
            'size',
            'color',
            'rented_date',
            'return_date',
            'map_url',
            'is_rented',
            'stripe_token',
            'renter_email',
            'renter_id',
            
        )