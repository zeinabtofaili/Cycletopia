from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.
class UsedBike(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    grouping = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=255)
    price = models.CharField(max_length=10)
    image = models.ImageField(upload_to='uploads/')
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    sellerEmail = models.CharField(max_length=255)
    sellerPhoneNumber = models.CharField(max_length = 20)
    sold = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='selling_bikes', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/user-bike/{self.slug}/'

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