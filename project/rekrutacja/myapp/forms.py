from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Personal_data, Adress, High_school, Documents_matura, Documents_achivment, Documents_dyploma, Matura_results, Applications


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = Personal_data
        fields = ['pesel', 'first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'father_name', 'is_polish', 'sex']
    # pesel = forms.IntegerField()
    # first_name = forms.CharField()
    # second_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.CharField(widget=forms.EmailInput)
    # phone = forms.CharField()
    # date_of_birth = forms.DateField(widget=forms.Date)
    # father_name = forms.CharField()
    # is_polish = forms.BooleanField(widget=forms.BooleanInput)
    # sex = 