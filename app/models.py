from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class LoginPage(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class RegisterPage(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def _str__(self):
        return self.username


class message(models.Model):
    name = models.CharField(max_length=50)
    eamil = models.EmailField(max_length=50)
    message = models.TextField(default=True)

    def __str__(self):
        return self.name





        
            


 