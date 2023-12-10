#calculating points for each application

from myapp.models import Applications, Subjects, Matura_results
ApplicationList = Applications.objects.all()

def main():
    for user_application in ApplicationList:
        if user_application.major != "LEK" or "ARCH":
            CountPoints(user_application.major, user_application.user, user_application)

def CountPoints(major, user, user_application):
    score = Matura_results.objects.get(user=user)
    subject = Subjects.objects.get(major=major)
    if score.polski_p>=30 and score.angielski_p>=30 and score.matematyka_p>=30:
        M = max(score.matematyka_r*2.5, score.matematyka_p, score.matematyka_p+score.matematyka_r*1.5)
        JO = max(score.angielski_p*0.1, score.angielski_r*0.25)
        JP = max(score.polski_p*0.1, score.polski_r*0.1)
        #TODO: add podstawowy poziom to calculating PD score :) (max(max(), max())
        PD = 2.5* max(score.fizyka_r, score.chemia_r*subject.chemia, score.biologia_r*subject.biologia, score.informatyka_r*subject.informatyka, score.geografia_r*subject.geografia)
        if M>0:
            user_application.is_condition = True
            user_application.score = sum(M, JO, JP, PD)
        else:
            user_application.is_condition = False
    else:
        user.is_condition = False