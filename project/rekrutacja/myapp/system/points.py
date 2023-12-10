#calculating points for each application

from myapp.models import Application
Applications = Application.objects.all()

def main():
    for user_application in Applications:
        CountPoints(user_application.user)

def CountPoints(user):
    pass