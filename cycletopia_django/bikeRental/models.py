from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import json
# Create your models here.
class RentPriceField(models.TextField):
    description = "A field to store rental duration and price pairs"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = {}
        kwargs['null'] = True
        kwargs['blank'] = True
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        if not value:
            value = {}
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except ValueError:
                pass
        return value

    def get_prep_value(self, value):
        if not value:
            value = {}
        if isinstance(value, dict):
            value = json.dumps(value)
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return str(value)


class RentalProduct(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    rent_duration_and_price = RentPriceField(null=True)
    user = models.ForeignKey(User, related_name='rented_products', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    grouping = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    rented_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    map_url = models.CharField(max_length=255, blank=True, null=True)
    is_rented = models.BooleanField(default=False)
    renter_email = models.CharField(max_length=255, blank=True, null=True)
    renter_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_token = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/rent-bike/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        
        if self.image:
            self.thumbnail = self.make_thumbnail(self.image)
            self.save()
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def save(self, *args, **kwargs):
        if self.return_date is None:
            self.is_rented = False
            self.rent_date = None
            self.return_date = None
            self.renter_email = None
            self.renter_id = None

        super(RentalProduct, self).save(*args, **kwargs)