from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
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
    # path('settings/', views.user_settings, name='settings'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('qualify_stack/', views.qualify_stack_view, name='qualify_stack'),
    path('qualify_sort/', views.qualify_sort_view, name='qualify_sort'),
    path('change-password/', PasswordChangeView.as_view(), name='password_change'),
    path('change-password/done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('calculate_score/', views.calculate, name='score_calculate')
]
