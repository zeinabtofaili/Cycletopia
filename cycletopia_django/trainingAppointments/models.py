from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TrainingAppointment(models.Model):
    user = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE, blank=True, null=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    time = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    bike_type = models.CharField(max_length=20)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.user.username
    
