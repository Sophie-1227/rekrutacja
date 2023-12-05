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
        fields = ['pesel', 'first_name', 'second_name', 'last_name', 'email', 'phone', 'father_name', 'is_polish', 'sex']
        labels = {
            'pesel': 'PESEL',
            'first_name': 'Imię',
            'second_name': 'Drugie imię',
            'last_name': 'Nazwisko',
            'email': 'Adres e-mail',
            'phone': 'Numer telefonu',
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
            'sex': forms.Select(attrs={'class': 'input'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['country', 'postal_code', 'city', 'street', 'building_number', 'apartment_number']
        labels = {
            'country': 'Kraj',
            'city': 'Miasto',
            'street': 'Ulica',
            'building_number': 'Numer budynku',
            'apartment_number': 'Numer mieszkania',
            'postal_code': 'Kod pocztowy',
        }
        widgets = {
            'country': forms.TextInput(attrs={'class': 'input'}),
            'postal_code': forms.TextInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'street': forms.TextInput(attrs={'class': 'input'}),
            'building_number': forms.TextInput(attrs={'class': 'input'}),
            'apartment_number': forms.TextInput(attrs={'class': 'input'}),
        }