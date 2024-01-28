import random
from myapp.models import Matura_results, Applications, Majors
from django.contrib.auth.models import User

USERS_NUMBER = 15000


def create_users(num_users=USERS_NUMBER):
    for i in range(num_users):
        User.objects.create(username=f'user{i}', password='password')


def create_scores():
    for user in User.objects.all():
        Matura_results.objects.filter(user_id=user).update(
            polski_p=random.randint(0, 100),
            polski_r=random.randint(0, 100),
            matematyka_p=random.randint(0, 100),
            matematyka_r=random.randint(0, 100),
            angielski_p=random.randint(0, 100),
            angielski_r=random.randint(0, 100),
            fizyka_r=random.randint(0, 100),
            chemia_r=random.randint(0, 100),
            geografia_r=random.randint(0, 100),
            biologia_r=random.randint(0, 100),
            informatyka_r=random.randint(0, 100)
        )


def create_passing_scores():
    for user in User.objects.all():
        Matura_results.objects.filter(user_id=user).update(
            polski_p=random.randint(30, 100),
            polski_r=random.randint(0, 100),
            matematyka_p=random.randint(30, 100),
            matematyka_r=random.randint(0, 100),
            angielski_p=random.randint(30, 100),
            angielski_r=random.randint(0, 100),
            fizyka_r=random.randint(0, 100),
            chemia_r=random.randint(0, 100),
            geografia_r=random.randint(0, 100),
            biologia_r=random.randint(0, 100),
            informatyka_r=random.randint(0, 100)
        )


def generate_applications():
    all_majors = Majors.objects.values_list('major', flat=True)
    for user in User.objects.all():
        new_application = Applications(
            preference=1,
            faculty='W10',
            major=random.choice(all_majors),
            tour=1,
            is_active=True,
            is_paid=True,
            user_id=user.id
        )

        new_application.save()


def generate_applications_multiple_preferences():
    all_majors = Majors.objects.values_list('major', flat=True)
    for user in User.objects.all():
        n = random.randint(1, 4)
        for i in range(n):
            new_application = Applications(
                preference=i,
                faculty='W10',
                major=random.choice(all_majors),
                tour=1,
                is_active=True,
                is_paid=True,
                user_id=user.id
            )

        new_application.save()
