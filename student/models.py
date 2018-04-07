from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True)

    class Meta:
        ordering = ('username',)