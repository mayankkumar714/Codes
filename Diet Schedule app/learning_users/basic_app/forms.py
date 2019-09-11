from django import forms
from django.contrib.auth.models import User
from basic_app.models import Schedule
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class ScheduleForm(forms.ModelForm):
    class Meta():
        model = Schedule
        fields =('food_item','number_of_times','duration')