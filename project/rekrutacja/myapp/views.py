from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import User, Personal_data, AuthUser


def index(request):
    return render(request, 'index.html')

# signup page


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page


def user_logout(request):
    logout(request)
    return redirect('login')

# dane osobowe


def user_dane_osobowe(request):
    if request.method == 'POST':
        form = PersonalDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonalDataForm()

    return render(request, 'personal_data.html', {'form': form})

# wyksztalcenie


def user_wyksztalcenie(request):
    # TODO: implement user_wyksztalcenie and create html page
    return render(request, 'wyksztalcenie.html')


def user_matura(request):
    if request.method == 'POST':
        form = MaturaDocumentsForm(request.POST)
        form_results = MaturaResultsForm(request.POST)
        if form.is_valid() and form_results.is_valid():
            form.save()
            form_results.save()
    else:
        form = MaturaDocumentsForm()
        form_results = MaturaResultsForm()

    return render(request, 'matura.html', {'form': form, 'form_results': form_results})


def user_osiagniecia(request):
    if request.method == 'POST':
        form = AchivmentDocumentsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AchivmentDocumentsForm()

    return render(request, 'achivments.html', {'form': form})


def user_dyplom(request):
    if request.method == 'POST':
        form = DyplomaDocumentsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DyplomaDocumentsForm()

    return render(request, 'dyplom.html', {'form': form})

# adres


def user_adres(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddressForm()

    return render(request, 'adres.html', {'form': form})


def user_zgloszenia(request):
    # TODO implement user_zgloszenia and create html page
    pass


def user_ofer(request):
    # TODO: implement user_ofer and create html page
    pass


def user_settings(request):
    # TODO: implement user_settings and create html page
    pass


def usun_rekordy(request):
    Personal_data.objects.all().delete()
    AuthUser.objects.all().delete()
    return render(request, 'usun_rekordy.html')
