from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.