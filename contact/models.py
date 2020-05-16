from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+' )
    location=models.CharField("Your Location", max_length=100,null=True,blank=True)
    phone=models.CharField("Contact Number", max_length=100,null=True,blank=True)
    email=models.CharField("Email", max_length=200,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.location