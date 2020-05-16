from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=models.CharField("Write Phone Name", max_length=100,null=True,blank=True)
    image=models.ImageField("Upload Client Image",null=True,blank=True)
    gender=models.CharField("Write gender", max_length=100,null=True,blank=True)
    position=models.CharField("Designation", max_length=100,null=True,blank=True)
    email_confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return f'{self.user.username} Profile'


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    # def save(self, force_insert=False, *args, **kwargs):
    #     super(Profile,self).save(force_insert,*args, **kwargs)

    #     img = Image.open(self.image.url)

    #     if img.height > 500 or img.width > 500:
    #         output_size = (500, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.image.url)       
