from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from myapp.models import Personal_data, Adress, High_school, Documents_matura, Documents_achivment, Documents_dyploma, Matura_results, Applications
from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# def cerateProfile(request):
#     id = request.user.id


# @receiver(post_save, instance=User)
# def create_user_profile(instance, created):
#     if created:
#         user_id_value = instance.id
#         Personal_data.objects.create(ID = user_id_value)
#         Adress.objects.create(ID = user_id_value)
#         High_school.objects.create(ID = user_id_value)
#         Documents_matura.objects.create(ID = user_id_value)
#         Documents_achivment.objects.create(ID = user_id_value)
#         Documents_dyploma.objects.create(ID = user_id_value)
#         Matura_results.objects.create(ID = user_id_value)
#         Applications.objects.create(ID = user_id_value)