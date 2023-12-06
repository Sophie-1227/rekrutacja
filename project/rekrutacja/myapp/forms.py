from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Personal_data, Adress, High_school, Documents_matura, Documents_achivment, Documents_dyploma, Matura_results, Applications

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']
        labels = {'username':'Login', 
                  'password1':'Hasło', 
                  'password2':'Potwierdź hasło',}

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

class HighSchoolForms(forms.Form):
    class Meta:
        model = High_school
        fields = ['school_type', 'school_name', 'school_country', 'school_city']
        widgets = {
            'school_type': 'Rodzaj szkoły',
            'school_name': 'Nazwa szkoły',
            'school_country': 'Państwo',
            'school_city': 'Miasto',
        }
        widgets = {
            'school_type': forms.TextInput(attrs={'class': 'input'}),
            'school_name': forms.TextInput(attrs={'class': 'input'}),
            'school_country': forms.TextInput(attrs={'class': 'input'}),
            'school_city': forms.TextInput(attrs={'class': 'input'}),
        }

class MaturaDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents_matura
        fields = ['exam_type', 'exam_number', 'exam_issuer', 'exam_city', 'exam_country']
        labels = {
            'exam_type': 'Rodzaj matury',
            # 'exam_year': 'Rok zdawania matury',
            'exam_number': 'Numer dokumentu',
            'exam_issuer': 'Nazwa instytucji wystawiającej',
            # 'exam_date': 'Data wydania',
            'exam_city': 'Miasto wydania',
            'exam_country': 'Kraj wydania',
        }
        widgets = {
            'exam_type': forms.TextInput(attrs={'class': 'input'}),
            # 'exam_year': forms.NumberInput(attrs={'class': 'input'}),
            'exam_number': forms.TextInput(attrs={'class': 'input'}),
            'exam_issuer': forms.TextInput(attrs={'class': 'input'}),
            # 'exam_date': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'exam_city': forms.TextInput(attrs={'class': 'input'}),
            'exam_country': forms.TextInput(attrs={'class': 'input'}),
        }

class AchivmentDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents_achivment
        fields = ['achivment_type', 'achivment_issuer', 'achivment_city', 'achivment_country']
        labels = {
            'achivment_type': 'Rodzaj dokumentu',
            # 'achivment_year': 'Rok uzyskania dokumentu',
            'achivment_issuer': 'Nazwa instytucji wystawiającej',
            'achivment_city': 'Miasto wydania',
            'achivment_country': 'Kraj wydania',
        }
        widgets = {
            'achivment_type': forms.TextInput(attrs={'class': 'input'}),
            # 'achivment_year': forms.NumberInput(attrs={'class': 'input'}),
            'achivment_issuer': forms.TextInput(attrs={'class': 'input'}),
            'achivment_city': forms.TextInput(attrs={'class': 'input'}),
            'achivment_country': forms.TextInput(attrs={'class': 'input'}),
        }

class DyplomaDocumentsForm(forms.ModelForm):
    class Meta:
        model = Documents_dyploma
        fields = ['dyploma_type', 'dyploma_result', 'dyploma_avg', 'dyploma_issuer', 'dyploma_city', 'dyploma_country']
        labels = {
            'dyploma_type': 'Rodzaj dyplomu',
            'dyploma_result': 'Ocena na dyplomie',
            'dyploma_avg': 'Średnia ważona z przebiegu studiów',
            # 'dyploma_year': 'Rok uzyskania dokumentu',
            'dyploma_issuer': 'Nazwa instytucji wystawiającej',
            'dyploma_city': 'Miasto wydania',
            'dyploma_country': 'Kraj wydania',
        }
        widgets = {
            'dyploma_type': forms.TextInput(attrs={'class': 'input'}),
            'dyploma_result': forms.TextInput(attrs={'class': 'input'}),
            'dyploma_avg': forms.NumberInput(attrs={'class': 'input'}),
            # 'dyploma_year': forms.NumberInput(attrs={'class': 'input'}),
            'dyploma_issuer': forms.TextInput(attrs={'class': 'input'}),
            'dyploma_city': forms.TextInput(attrs={'class': 'input'}),
            'dyploma_country': forms.TextInput(attrs={'class': 'input'}),
        }

class MaturaResultsForm(forms.ModelForm):
    class Meta:
        model = Matura_results
        fields = [
            'polski_p', 'polski_r', 'matematyka_p', 'matematyka_r',
            'angielski_p', 'angielski_r', 'fizyka_p', 'fizyka_r',
            'chemia_p', 'chemia_r', 'geografia_p', 'geografia_r',
            'biologia_p', 'biologia_r', 'informatyka_p', 'informatyka_r'
        ]
        labels = {
            'polski_p': 'Polski Poziom Podstawowy',
            'polski_r': 'Polski Poziom Rozszerzony',
            'matematyka_p': 'Matematyka Poziom Podstawowy',
            'matematyka_r': 'Matematyka Poziom Rozszerzony',
            'angielski_p': 'Angielski Poziom Podstawowy',
            'angielski_r': 'Angielski Poziom Rozszerzony',
            'fizyka_p': 'Fizyka Poziom Podstawowy',
            'fizyka_r': 'Fizyka Poziom Rozszerzony',
            'chemia_p': 'Chemia Poziom Podstawowy',
            'chemia_r': 'Chemia Poziom Rozszerzony',
            'geografia_p': 'Geografia Poziom Podstawowy',
            'geografia_r': 'Geografia Poziom Rozszerzony',
            'biologia_p': 'Biologia Poziom Podstawowy',
            'biologia_r': 'Biologia Poziom Rozszerzony',
            'informatyka_p': 'Informatyka Poziom Podstawowy',
            'informatyka_r': 'Informatyka Poziom Rozszerzony',
        }
        widgets = {
            'polski_p': forms.NumberInput(attrs={'class': 'input'}),
            'polski_r': forms.NumberInput(attrs={'class': 'input'}),
            'matematyka_p': forms.NumberInput(attrs={'class': 'input'}),
            'matematyka_r': forms.NumberInput(attrs={'class': 'input'}),
            'angielski_p': forms.NumberInput(attrs={'class': 'input'}),
            'angielski_r': forms.NumberInput(attrs={'class': 'input'}),
            'fizyka_p': forms.NumberInput(attrs={'class': 'input'}),
            'fizyka_r': forms.NumberInput(attrs={'class': 'input'}),
            'chemia_p': forms.NumberInput(attrs={'class': 'input'}),
            'chemia_r': forms.NumberInput(attrs={'class': 'input'}),
            'geografia_p': forms.NumberInput(attrs={'class': 'input'}),
            'geografia_r': forms.NumberInput(attrs={'class': 'input'}),
            'biologia_p': forms.NumberInput(attrs={'class': 'input'}),
            'biologia_r': forms.NumberInput(attrs={'class': 'input'}),
            'informatyka_p': forms.NumberInput(attrs={'class': 'input'}),
            'informatyka_r': forms.NumberInput(attrs={'class': 'input'}),
        }

# class ApplicationsForm(forms.ModelForm):
#     class Meta:
#         model = Applications
#         fields = [
#             'preference', 'faculty', 'major', 'tour', 'is_active',
#             'is_condition', 'score', 'is_paid', 'is_qualified',
#             'are_documents', 'decision'
#         ]
#         labels = {
#             'preference': 'Preferencja',
#             'faculty': 'Wydział',
#             'major': 'Kierunek',
#             'tour': 'Tur',
#             'is_active': 'Aktywne',
#             'is_condition': 'Warunkowe',
#             'score': 'Wynik',
#             'is_paid': 'Opłacone',
#             'is_qualified': 'Zakwalifikowane',
#             'are_documents': 'Dokumenty dostarczone',
#             'decision': 'Decyzja'
#         }
#         widgets = {
#             'preference': forms.NumberInput(attrs={'class': 'input'}),
#             'faculty': forms.TextInput(attrs={'class': 'input'}),
#             'major': forms.TextInput(attrs={'class': 'input'}),
#             'tour': forms.NumberInput(attrs={'class': 'input'}),
#             'is_active': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#             'is_condition': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#             'score': forms.NumberInput(attrs={'class': 'input'}),
#             'is_paid': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#             'is_qualified': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#             'are_documents': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#             'decision': forms.CheckboxInput(attrs={'class': 'input-checkbox'}),
#         }