from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    # Add any additional attributes you want
    
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    created_date = models.DateTimeField(default=timezone.now)
    desciption = models.CharField(max_length=500,default='Action')
    categories = models.CharField(max_length=20,default='Action')
    tags = models.CharField(max_length=10,default='DEFAULT')
    reference_Id = models.CharField(max_length=20,default='DEFAULT')

    def __str__(self):
        return str(self.videofile)
