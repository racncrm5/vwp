from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from vwp_app.models import Tbluser, Tblpartner, Tblbankinfo, Tblproperty, Tblinvestment, TblLog
from django.db import models
from vwp_app.forms import AddUserForm, UserProfileInfoFrm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create a stabase connection
def index(request):
    user_list = Tbluser.objects.filter(user_status='Active')
    users = {}
    for user in user_list:
        users[user.user_name] = user.user_password

    user_dict = {'users_l':users}
    print(users)
    return render(request,'vwp_app/index.html',context=user_dict)
    # Create your views here
#    user_list = Tbluser.objects.order_by('user_name')
#    user_dict = {'user_list':user_list}
#    return render(request,'vwp_app/index.html',context=user_dict)

def help(request):
    help_dict = {'help_me': 'Click on Me!<a href="www.google.com">MEEE</a>'}
    return render(request,'vwp_app/help.html',context=help_dict)

def mainvwp(request):
    main_dict = {'main_temp': 'This is the main webpage',
                 'salute':'Good Bye Loser'}
    return render(request,'vwp_app/mainvwp.html', context=main_dict)

def adduser(request):

    form = AddUserForm()

    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error')

    return render(request,'vwp_app/adduser.html',{'adduser':form})

def registration(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoFrm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True
            else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoFrm()

    return render(request,'vwp_app/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})

def relative(request):
    return render(request,'vwp_app/relativeurl.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainvwp'))

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('mainvwp'))
            else:
                return HttpResponse("Account is not Active")
        else:
            print("some failed login")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login credentials")
    else:
        return render(request,'vap_app/login.html', {})

# def frm_add_user_view(request):
#     form = forms.FormAddUser()
#
#     if request.method == 'POST':
#         form = forms.FormAddUser(request.POST)
#
#         if form.is_valid():
#             print(form.cleaned_data['user_name'])
#             print(form.cleaned_data['user_status'])
#     return render(request,'vwp_app/adduser.html',{'add_user':form})
