from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, serialize=False)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=50)
    
    