from django.shortcuts import render
from basic_app.forms import UserForm,ScheduleForm,UserProfileInfoForm
from django.views.generic import TemplateView
from .models import Schedule

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        
        if user_form.is_valid() and profile_form.is_valid():

            
            user = user_form.save()

            
            user.set_password(user.password)

            user.save()


            profile = profile_form.save(commit=False)

            
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(username=username, password=password)

        
        if user:
            
            if user.is_active:
                
                login(request,user)
                
                return HttpResponseRedirect(reverse('index'))
            else:
           
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        
        return render(request, 'basic_app/login.html', {})


@login_required
def new_schedule(request):
    
    if request.method =='POST':
        food_item = request.POST.get('food_item')
        number_of_times = request.POST.get('number_of_times')
        duration = request.POST.get('duration')

        t = Schedule(food_item=food_item,number_of_times=number_of_times,duration=duration)
        t.save()

    form = ScheduleForm()
    return render(request,'basic_app/create_schedule.html',{'form':form})
    
@login_required
def view_schedule(request):
    full_schedule=Schedule.objects.all()

    return render(request,'basic_app/view_diet.html',{'Items':full_schedule})
