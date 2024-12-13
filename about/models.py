from django.db import models
from django_summernote.fields import SummernoteTextField
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title