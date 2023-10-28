from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    map_url = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    attendees = models.ManyToManyField(User, blank=True)
    date_and_time = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/cycling-events/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
