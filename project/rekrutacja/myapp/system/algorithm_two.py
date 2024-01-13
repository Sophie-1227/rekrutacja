from myapp.models import Applications, Majors, Matura_results
# from project.rekrutacja.myapp.points import CountPoints
import numpy as np

#TODO: add option that there is a draw in score and we will extend a list
#TODO: OPTIONAL add option of min score for certain majors

# qualifiedUsers = []
majors_fields = Majors.objects.all()

#NOTE: dictionary to store vectors
qualified_users_vector = {}

for major in majors_fields:
    vector = np.zeros(major.limit, dtype=np.object)
    majors_fields[major.major] = vector

def qualifyHighestPreferences():
    ApplicationList = Applications.objects.filter(preference = 1)
    for record in ApplicationList:
         CountPoints(record.major, record.user)
    SortedApplication = Applications.objects.filter(preference = 1).order_by('score')
    for application in SortedApplication:
        if majors_fields[application.major][-1] is 'None':
            #NOTE: Jest jeszcze miejsce na kierunku
            none_index = np.where(vector == None)[0]
            majors_fields[application.major][none_index] = application.user
            # qualifiedUsers.append([application.user, application.preference])
            application.is_qualified = True
        else:
            #NOTE: Nie ma już miejsca na kierunku
            application.is_qualified = False
            #TODO: Add choosable field why isnt qualified
    ApplicationList.delete()
    #TODO: Add STOP rule
    #NOTE: Stop rule: for each user there must be an application with status true or none with status NONE (all are false)
    for user in Applications.objects.values('user').distinct():
        if Applications.objects.filter(user=user, is_qualified=True).exists():
            userTopApplication = Applications.objects.filter(user=user, is_qualified__isnull=True).order_by("preference").first()
            ApplicationList.append(userTopApplication)
    for record in ApplicationList:
         CountPoints(record.major, record.user)
    qualifyFromList(ApplicationList)

def qualifyFromList(ApplicationList):
    SortedApplication = Applications.objects.filter(preference = 1).order_by('score')
    for application in SortedApplication:
        if majors_fields[application.major][-1] is 'None':
            #NOTE: Jest jeszcze miejsce na kierunku
            none_index = np.where(vector == None)[0]
            majors_fields[application.major][none_index] = application.user
            # qualifiedUsers.append([application.user, application.preference])
            application.is_qualified = True
        else:
            #NOTE: Nie ma już miejsca na kierunku
            #TODO: Add option of higher score then last candidate
            if application.score > majors_fields[application.major][-1][7]: #7 is score
                #Wyrzucenie oststniego kandydata z listy
                oldUser = majors_fields[application.major][-1][0]
                oldApplication = Applications.objects.filter(user=oldUser, major=application.major)
                oldApplication.is_qualified = False
                #Przyjęcie nowego kandydata na kierunek
                majors_fields[application.major][none_index] = application.user
                # qualifiedUsers.append([application.user, application.preference])
                application.is_qualified = True

            else:
                #NOTE: Ma niższy wskaźnik niż ostatnia osoba na liście
                application.is_qualified = False
            #TODO: Add choosable field why isnt qualified
