from django.db import models
from cloudinary.models import CloudinaryField

INTERESTS = (("Makeup Interest", "Makeup"), ("Hair Interest", "Hair"), ("Other Interest", "Other"))

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    
    class Meta:
        ordering = ["updated_on"]

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    interest = models.TextField(choices=INTERESTS)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Collaboration request from {self.name}"