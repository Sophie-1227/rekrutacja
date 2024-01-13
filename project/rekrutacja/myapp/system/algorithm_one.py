from myapp.models import Applications, Majors, Matura_results
# from project.rekrutacja.myapp.points import CountPoints
import numpy as np

#TODO: add option that there is a draw in score and we will extend a list
#TODO: OPTIONAL add option of min score for certain majors

qualifiedUsers = []
majors_fields = Majors.objects.all()

#NOTE: dictionary to store vectors
qualified_users_vector = {}

for major in majors_fields:
    vector = np.zeros(major.limit, dtype=np.object)
    majors_fields[major.major] = vector

def qualifyAllPreferences():
    ApplicationList = Applications.objects.all()
    for record in ApplicationList:
        CountPoints(record.major, record.user)
    SortedApplication = Applications.objects.all().order_by('score')
    for application in SortedApplication:
        is_qualified = any(application.user == row[0] for row in qualifiedUsers)
        if is_qualified:
            #NOTE: Był wcześniej zakwalifikowany
            previous_preference = [row[1] for row in qualifiedUsers if row[0] == application.user]
            if application.preference < previous_preference:
                #NOTE: Bardziej mu zależy na tej preferencji
                if majors_fields[application.major][-1] is 'None':
                    #NOTE: Nie ma miejsc na kierunku
                    #TODO: Co się stanie jak się zwolni miejsce jeśli zwolnimy poprzednio zajmowane miejsce
                    pass
                else:
                    #NOTE: Są miejsca, więc dopisujemy i wypisujemy z poprzedniego
                    pass
                #TODO: Add new loop for applications in between
            else:
                #NOTE: Mniej mu zależy na tej preferencji
                application.is_qualified = False
                #TODO: add choosable field why isnt qualified        
        else:
            #NOTE: Nie był wcześniej zakwalifikowany
            if majors_fields[application.major][-1] is 'None':
                #NOTE: Jest jeszcze miejsce na kierunku
                none_index = np.where(vector == None)[0]
                majors_fields[application.major][none_index] = application.user
                qualifiedUsers.append([application.user, application.preference])
                application.is_qualified = True
            else:
                #NOTE: Nie ma już miejsca na kierunku
                application.is_qualified = False
                #TODO: Add choosable field why isnt qualified