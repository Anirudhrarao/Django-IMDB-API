from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Movie Name")
    description = models.CharField(max_length=200, verbose_name="Description")
    active = models.BooleanField(default=True, verbose_name="Active")
    
    def __str__(self):
        return self.name
    