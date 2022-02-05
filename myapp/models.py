from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from django.db import models

class Response_pdf(models.Model):
    text_content=models.CharField(max_length=1000)
    image_content=models.ImageField(upload_to='images/')

# Create your models here.
