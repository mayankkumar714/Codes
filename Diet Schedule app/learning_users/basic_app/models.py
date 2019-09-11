from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    
    user = models.OneToOneField(User,on_delete=models.CASCADE,)

    
    portfolio_site = models.URLField(blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        
        return self.user.username

class Schedule(models.Model):

        food_item = models.TextField()
        number_of_times = models.IntegerField()
        duration = models.CharField(max_length=200)

        def __str__(self):
            return self.food_item
