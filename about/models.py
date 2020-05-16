from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class About(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+')
    description=models.TextField("Write About You",null=True,blank=True)
    image=models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "About"


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

class Service(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+')
    service=models.CharField("Title Of Your Service", max_length=100,null=True,blank=True)
    service_icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    service_des=models.TextField("Service Detail",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Service"

    def __str__(self):
        return self.service


class Client(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+')
    client_name=models.CharField("Name Of Client", max_length=100,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    link=models.TextField("Link Of Client",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Client"

    def __str__(self):
        return self.client_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Facts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+' )
    fact_icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    fact_title=models.CharField("Fact Title",max_length=100,null=True,blank=True)
    count=models.CharField("Fact total Number", max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Fact"

    def __str__(self):
        return self.fact_title

class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+' )
    name=models.CharField("Write Client Name", max_length=100,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    position=models.CharField("Designation", max_length=100,null=True,blank=True)
    des=models.TextField("Client Words",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
