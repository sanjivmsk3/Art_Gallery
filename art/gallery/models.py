from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='art/')

    def __str__(self):
        return self.title


