from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+' )
    name=models.CharField(max_length=100,null=True,blank=True,unique=True)
    slug= models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
pre_save.connect(rl_pre_save_receiver, sender=Category)



class portfolio(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='+' )
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    link=models.CharField(max_length=100,null=True,blank=True)
    title=models.CharField(max_length=100,null=True,blank=True)
    icon=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.title)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


