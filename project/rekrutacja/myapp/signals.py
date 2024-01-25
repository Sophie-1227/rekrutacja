from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import User
from myapp.models import AuthUser, Personal_data, Adress, High_school, Documents_matura, Documents_achivment, Documents_dyploma, Matura_results, Applications
from django.db import models


@receiver(post_save, sender=AuthUser)
def create_user_profile_and_preferences(sender, instance, created, **kwargs):
    print("Hello? Are you here?")
    if created:
        Personal_data.objects.create(user=instance)
        Adress.objects.create(user=instance)
        High_school.objects.create(user=instance)
        Documents_matura.objects.create(user=instance)
        Documents_achivment.objects.create(user=instance)
        Documents_dyploma.objects.create(user=instance)
        Matura_results.objects.create(user=instance)
