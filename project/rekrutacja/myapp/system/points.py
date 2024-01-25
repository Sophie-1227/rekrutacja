# calculating points for each application

from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Applications, Matura_results, Majors


def calculate_score(request):
    major = request.GET.get('major')
    user = request.GET.get('user')
    score = float(request.GET.get('score'))
    is_condition = False

    applications = Applications.objects.filter(user=user)
    wyniki_matury = Matura_results.objects.filter(application__in=applications)

    for application in applications:
        for wynik_matury in wyniki_matury:
            # Implementacja algorytmu dla matury IB
            if application.exam_type == 'maturaIB':
                inputValue = wynik_matury.input_value
                table_value = 0
                if inputValue == 7 or inputValue == 6:
                    table_value = 100
                elif inputValue == 5:
                    table_value = 85
                elif inputValue == 4:
                    table_value = 70
                elif inputValue == 3:
                    table_value = 55
                elif inputValue == 2:
                    table_value = 40
                elif inputValue == 1:
                    table_value = 0
                wynik_matury.table_value = table_value
                wynik_matury.save()

    # Implementacja algorytmu dla nowaMatura
    polski_p = float(request.GET.get('polski_p'))
    angielski_p = float(request.GET.get('angielski_p'))
    matematyka_p = float(request.GET.get('matematyka_p'))

    if polski_p >= 30 and angielski_p >= 30 and matematyka_p >= 30:
        exam_type = request.GET.get('exam_type')
        if exam_type == 'nowaMatura':
            fizyka = float(request.GET.get('fizyka'))
            chemia = float(request.GET.get('chemia'))
            biologia = float(request.GET.get('biologia'))
            informatyka = float(request.GET.get('informatyka'))
            geografia = float(request.GET.get('geografia'))
            PD = 2.5 * max(fizyka, chemia, biologia, informatyka, geografia)
        else:
            fizyka_r = float(request.GET.get('fizyka_r'))
            chemia_r = float(request.GET.get('chemia_r'))
            biologia_r = float(request.GET.get('biologia_r'))
            informatyka_r = float(request.GET.get('informatyka_r'))
            geografia_r = float(request.GET.get('geografia_r'))

            fizyka_p = float(request.GET.get('fizyka_p'))
            chemia_p = float(request.GET.get('chemia_p'))
            biologia_p = float(request.GET.get('biologia_p'))
            informatyka_p = float(request.GET.get('informatyka_p'))
            geografia_p = float(request.GET.get('geografia_p'))

            PD = max(
                2.5 * max(fizyka_r, chemia_r, biologia_r,
                          informatyka_r, geografia_r),
                max(fizyka_p, chemia_p, biologia_p, informatyka_p, geografia_p),
                max(fizyka_p + fizyka_r * 1.5, chemia_p + chemia_r * 1.5,
                    biologia_p + biologia_r * 1.5, informatyka_p + informatyka_r * 1.5,
                    geografia_p + geografia_r * 1.5)
            )

        matematyka_r = float(request.GET.get('matematyka_r'))
        M = max(matematyka_r * 2.5, matematyka_p,
                matematyka_p + matematyka_r * 1.5)
        JO = max(angielski_p * 0.1, float(request.GET.get('angielski_r')) * 0.25)
        JP = 0.1 * max(polski_p, float(request.GET.get('polski_r')))
        is_condition = True
        score = M + JO + JP + PD
    else:
        is_condition = False

    # Wynik w formie JSON
    result = {
        'score': score,
        'is_condition': is_condition,
    }
    return JsonResponse(result)
