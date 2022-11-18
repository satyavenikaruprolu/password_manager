from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100,null=False, unique=True)
    pwd = models.CharField(max_length=50,null=False)    
    loggedin= models.BooleanField(default=False)
    

class Password(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    domain_name = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=50,null=False)
