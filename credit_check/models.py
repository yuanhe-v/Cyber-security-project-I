from django.db import models
from django.contrib.auth.models import User
#from django_cryptography.fields import encrypt


class Course(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.TextField()
    
    #ssn = encrypt(models.TextField())
    ssn = models.TextField()
    
    


