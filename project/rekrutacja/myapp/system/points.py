#calculating points for each application

from myapp.models import Applications, Majors, Matura_results
ApplicationList = Applications.objects.all()

def main():
    for user_application in ApplicationList:
        if user_application.major != "LEK" or "ARCH":
            CountPoints(user_application.major, user_application.user, user_application.score, user_application.is_condition)

def CountPoints(major, user, score, is_condition):
    score = Matura_results.objects.get(user=user)
    subject = Majors.objects.get(major=major)
    if score.polski_p>=30 and score.angielski_p>=30 and score.matematyka_p>=30:    
        M = max(score.matematyka_r*2.5, score.matematyka_p, score.matematyka_p+score.matematyka_r*1.5)
        JO = max(score.angielski_p*0.1, score.angielski_r*0.25)
        JP = 0,1*max(score.polski_p, score.polski_r)
        #TODO: add podstawowy poziom to calculating PD score :) (max(max(), max())
        PD = max(2.5* max(score.fizyka_r, score.chemia_r*subject.chemia, score.biologia_r*subject.biologia, score.informatyka_r*subject.informatyka, score.geografia_r*subject.geografia),
                 max(score.fizyka_p, score.chemia_p*subject.chemia, score.biologia_p*subject.biologia, score.informatyka_p*subject.informatyka, score.geografia_p*subject.geografia ),
                 max(1.5*score.fizyka_r+score.fizyka_p, 1.5*score.chemia_r+score.chemia_p, 1.5*score.biologia_r+score.biologia_p, 1.5*score.informatyka_r+score.informatyka_p, 1.5*score.geografia_r+score.geografia_p))
        is_condition = True
        score = sum(M, JO, JP, PD)
    else:
        is_condition = False