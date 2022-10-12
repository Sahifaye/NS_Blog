from email.mime import image, message
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.views import get_forcast


# Create your views here.
def Register(request):
    messages = []
    print (">>>>")
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        name=request.POST['name']
        if name.__contains__(' '):
            first_name=name.split(" ")[0]
            last_name=name.split(" ")[1]
        else:
            first_name=name
            last_name=''
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1, password2)
        if password1 != password2:
            print(password1,">>>>>>>>>>>>>>>>>>>>>>>",password2)
            messages.append("Passwords do not match.")
            return render(request, 'base_templates/register.html',  {'messages':messages})
 
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.append("User Registered , Please Login with your credentials.")
        return render(request, 'base_templates/login.html', {'messages':messages}) 
    return render(request, 'base_templates/register.html',  {'messages':messages})


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        messages = []
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.append("Successfully Logged In")
            return redirect("home")
        else:
            messages.append("Username/Password not found OR Invalid Credentials")
            return render(request, 'base_templates/login.html', {'messages': messages})

    else:
        return render(request, 'base_templates/login.html', {})

@login_required()
def Logout(request):
    logout(request)
    return redirect("home")

@login_required()
def delete_ProfileImage(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    print(">?>>>>>???>>>>", request.user)
    q = Profile.objects.filter(user=request.user).update(image="")
    print(q)

    return JsonResponse({"response":True})

@login_required()
def EditProfile(request):
    
    forcast = get_forcast()
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    print(">>>>>>>",profile)
    if request.method == "POST":
        q_dict = {k:v for k, v in request.POST.items()}
        print(q_dict)
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        print("___________", form)
        if form.is_valid():
            form.save()
            message = "Data Saved Successfully"
            print("Data Saved Successfully .")
            return render(request, 'base_templates/profile.html', {})
        else:
            message = "Some Error in the Data Shared , Please check "
            print("Data Saved Successfully .")
            return render(request, 'base_templates/profile.html', {})
    else:
        profile_form = ProfileForm()
        return render(request, 'base_templates/profile.html', {'form':profile_form , 'forcast':forcast})
        # return render(request, 'base_templates/profile_form_test.html', {'form':profile_form})


