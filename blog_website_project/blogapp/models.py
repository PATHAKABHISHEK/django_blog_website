from django.db import models
from django.utils import timezone 


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.title



class Blog(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title
