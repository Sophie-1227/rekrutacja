# Django imports
# from myapp.models import Applications, Majors, Matura_results
# import sys
# sys.path.append('project//rekrutacja//myapp//')
# import models
# sys.path.remove('project//rekrutacja//myapp//')
# from project.rekrutacja.myapp.points import CountPoints
import numpy as np
from models import Applications

# TODO: add an option for a draw in score, and extend the list
# TODO: OPTIONAL add an option for a minimum score for certain majors

# qualifiedUsers = []
majors_fields = Majors.objects.all()

# NOTE: dictionary to store vectors
qualified_users_vector = {}

for major in majors_fields:
    vector = np.zeros(major.limit, dtype=np.object)
    majors_fields[major.major] = vector

def qualifyHighestPreferences():
    ApplicationList = Applications.objects.filter(preference=1)
    for record in ApplicationList:
        CountPoints(record.major, record.user)
    SortedApplication = Applications.objects.filter(preference=1).order_by('score')
    for application in SortedApplication:
        if majors_fields[application.major][-1] == 'None':
            # NOTE: There is still a place in the major
            none_index = np.where(vector == None)[0]
            majors_fields[application.major][none_index] = application.user
            # qualifiedUsers.append([application.user, application.preference])
            application.is_qualified = True
        else:
            # NOTE: There is no place in the major
            application.is_qualified = False
            # TODO: Add a choosable field to indicate why the application is not qualified
    ApplicationList.delete()
    # TODO: Add STOP rule
    # NOTE: Stop rule: for each user, there must be an application with status true or none with status NONE (all are false)
    for user in Applications.objects.values('user').distinct():
        if Applications.objects.filter(user=user, is_qualified=True).exists():
            userTopApplication = Applications.objects.filter(user=user, is_qualified__isnull=True).order_by("preference").first()
            ApplicationList.append(userTopApplication)
    for record in ApplicationList:
         CountPoints(record.major, record.user)
    qualifyFromList(ApplicationList)

def qualifyFromList(ApplicationList):
    SortedApplication = Applications.objects.filter(preference=1).order_by('score')
    for application in SortedApplication:
        if majors_fields[application.major][-1] == 'None':
            # NOTE: There is still a place in the major
            none_index = np.where(vector == None)[0]
            majors_fields[application.major][none_index] = application.user
            # qualifiedUsers.append([application.user, application.preference])
            application.is_qualified = True
        else:
            # NOTE: There is no place in the major
            # TODO: Add an option for a higher score than the last candidate
            if application.score > majors_fields[application.major][-1][7]:  # 7 is the score index
                # Remove the last candidate from the list
                oldUser = majors_fields[application.major][-1][0]
                oldApplication = Applications.objects.filter(user=oldUser, major=application.major)
                oldApplication.is_qualified = False
                # Accept the new candidate to the major
                majors_fields[application.major][none_index] = application.user
                # qualifiedUsers.append([application.user, application.preference])
                application.is_qualified = True
            else:
                # NOTE: Lower score than the last person on the list
                application.is_qualified = False
            # TODO: Add a choosable field to indicate why the application is not qualified
