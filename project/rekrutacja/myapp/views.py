from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Personal_data, AuthUser, Matura_results, Applications
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from .generate_test_data import *
from django.contrib.auth.forms import UserCreationForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')

# signup page


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# post_save.connect(create_user_profile_and_preferences, sender=User)


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
    # TODO: implement user_zgloszenia and create html page
    pass


def user_ofer(request):
    return render(request, 'offer.html')


# def user_settings(request):
#     # TODO: implement user_settings and create html page
#     pass


@csrf_exempt
def admin_view(request):
    generate_applications()
    return JsonResponse({'error': 'Data base updated'})


@csrf_exempt
def calculate(request):
    calculate_score(request=request)
    return JsonResponse({'sucess': 'Score calculation completed'})


@csrf_exempt
def qualify_sort_view(request):
    qualify_sort(request=request)
    return JsonResponse({'success': 'Lists have been rendered'})


def qualify_stack_view(request):
    qualify_stacks(request=request)
    return JsonResponse({'success': 'Lists have been rendered'})
