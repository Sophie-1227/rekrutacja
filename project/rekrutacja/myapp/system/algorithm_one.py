from myapp.models import Applications, Majors, Matura_results
from points import CountPoints

def qualifyAllPreferences():
    ApplicationList = Applications.objects.all()
    for record in ApplicationList:
        CountPoints(record.major, record.user)
    SortedApplication = Applications.objects.all().order_by('score')
    for application in SortedApplication:
        pass