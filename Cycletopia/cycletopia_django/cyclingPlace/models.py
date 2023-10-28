from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    map_url = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/cycling-places/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
