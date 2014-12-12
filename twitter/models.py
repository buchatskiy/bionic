from django.db import models

class Twit(models.Model):
    text=models.TextField(max_length=255)
# Create your models here.
