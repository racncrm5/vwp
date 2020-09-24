from django import forms
from django.core import validators
from vwp_app.models import Tbluser
from django.contrib.auth.models import User
from vwp_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoFrm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

def check_for_a(value):
    if value[0] != 'A':
        raise forms.ValidationError("Name needs to start with A")

# class FormAddUser(forms.Form):
#     user_name = forms.CharField(max_length=100)
#     user_password = forms.CharField(widget=forms.PasswordInput())
#     v_user_pwd = forms.CharField(widget=forms.PasswordInput(), label="Type in Password Again")
#     user_status = forms.CharField(validators=[check_for_a])
#     start_date = forms.DateField()
#     term_date = forms.DateField()
#
#     def clean(self):
#         all_clean_data = super().clean()
#         u_name = all_clean_data['user_name']
#         pwd = all_clean_data['user_password']
#         rpwd = all_clean_data['v_user_pwd']
#         print("all clean")
#
#         if pwd == rpwd:
#             print(u_name)

class AddUserForm(forms.ModelForm):
    class Meta:
        model = Tbluser
        exclude = ['user_id']
