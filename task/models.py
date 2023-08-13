from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=255, blank=True)


class PDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    location = models.CharField(max_length=255, blank=True)
