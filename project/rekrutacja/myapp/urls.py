from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('dane_osobowe/', views.user_dane_osobowe, name='dane_osobowe'),
    path('wyksztalcenie/', views.user_wyksztalcenie, name='wyksztalcenie'),
    path('wyksztalcenie/matura/', views.user_matura, name='matura'),
    path('wyksztalcenie/osiagniecia/', views.user_osiagniecia, name='achivments'),
    path('wyksztalcenie/dyplom/', views.user_dyplom, name='dyploma'),
    path('adres/', views.user_adres, name='adres'),
    path('zgloszenia/', views.user_zgloszenia, name='zgloszenia'),
    path('ofer/', views.user_ofer, name='ofer'),
    path('settings/', views.user_settings, name='settings'),
    path('calculate/', views.calculate_view, name='calculate_view'),
]
