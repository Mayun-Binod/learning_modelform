from django import forms
from django.core import validators
from enroll.models import User  
class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels={'name':'Enter the Name',"email":"Enter the Email","password":"Enter the password"}
        help_text={"name":"Enter your full Name"}
        error_messages={"name":{"required":"please write name"},'password':{"required":"password must be needed"}}
        widgets={'password':forms.PasswordInput,"name":forms.TextInput(attrs={"class":"myclass","placecholder":"This is placeholder"})}