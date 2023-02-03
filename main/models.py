from django.db import models
from django.contrib.auth.models import User



class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='main/images/')
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
