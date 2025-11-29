from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    #created_at = models.DateField(default=datetime.now())   
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title