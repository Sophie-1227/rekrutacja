from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Personal_data, Adress, High_school, Documents_matura, Documents_achivment, Documents_dyploma, Matura_results, Applications
from tempus_dominus.widgets import DatePicker

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
        fields = ['pesel', 'first_name', 'second_name', 'last_name', 'email', 'phone', 'date_of_birth', 'father_name', 'is_polish', 'sex']
        labels = {
            'pesel': 'PESEL',
            'first_name': 'Imię',
            'second_name': 'Drugie imię',
            'last_name': 'Nazwisko',
            'email': 'Adres e-mail',
            'phone': 'Numer telefonu',
            'date_of_birth': 'Data urodzenia',
            'father_name': 'Imię ojca',
            'is_polish': 'Czy posiadasz polskie obywatelstwo',
            'sex': 'Płeć',
        }
        widgets = {
            'pesel': forms.TextInput(attrs={'class': 'input'}),
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'second_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'phone': forms.TextInput(attrs={'class': 'input'}),
            'father_name': forms.TextInput(attrs={'class': 'input'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'input'}),
            'is_polish': forms.CheckboxInput(attrs={'class': 'input'}),
            'sex': forms.Select(attrs={'class': 'input'}),
        }