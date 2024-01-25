from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Applications, Matura_results, Majors, Documents_matura, AuthUser

# calculating points for each application


def calculate_score(request):
    applications = Applications.objects.all()

    for application in applications:
        user = application.user
        major = application.major
        PD_major = Majors.objects.filter(major=major)
        exam_type = Documents_matura.objects.filter(user=user)
        wyniki_matury = Matura_results.objects.filter(user=user)
        is_condition = False
        if exam_type == 'maturaIB':
            # Implementacja algorytmu dla matury IB
            for wynik in wyniki_matury:
                table_value = 0
                if wynik == 7 or wynik == 6:
                    table_value = 100
                elif wynik == 5:
                    table_value = 85
                elif wynik == 4:
                    table_value = 70
                elif wynik == 3:
                    table_value = 55
                elif wynik == 2:
                    table_value = 40
                elif wynik == 1:
                    table_value = 0
                Matura_results.filter(user=user).update(wynik=table_value)

    polski_p = wyniki_matury.polski_p
    angielski_p = wyniki_matury.angielski_p
    matematyka_p = wyniki_matury.matematyka_p
    polski_r = wyniki_matury.polski_r
    angielski_r = wyniki_matury.angielski_r
    matematyka_r = wyniki_matury.matematyka_r

    if polski_p >= 30 and angielski_p >= 30 and matematyka_p >= 30:
        if exam_type == 'nowaMatura':
            fizyka = wyniki_matury.fizyka_r * PD_major.fizyka
            chemia = wyniki_matury.chemia_r * PD_major.chemia
            biologia = wyniki_matury.biologia_r * PD_major.biologia
            informatyka = wyniki_matury.informatyka_r * PD_major.informatyka
            geografia = wyniki_matury.geografia_r * PD_major.geografia
            PD = 2.5 * max(fizyka, chemia, biologia, informatyka, geografia)
        else:
            fizyka_r = wyniki_matury.fizyka_r * PD_major.fizyka
            chemia_r = wyniki_matury.chemia_r * PD_major.chemia
            biologia_r = wyniki_matury.biologia_r * PD_major.biologia
            informatyka_r = wyniki_matury.informatyka_r * PD_major.informatyka
            geografia_r = wyniki_matury.geografia_r * PD_major.geografia

            fizyka_p = wyniki_matury.fizyka_p * PD_major.fizyka
            chemia_p = wyniki_matury.chemia_p * PD_major.chemia
            biologia_p = wyniki_matury.biologia_p * PD_major.biologia
            informatyka_p = wyniki_matury.informatyka_p * PD_major.informatyka
            geografia_p = wyniki_matury.geografia_p * PD_major.geografia

            PD = max(
                2.5 * max(fizyka_r, chemia_r, biologia_r,
                          informatyka_r, geografia_r),
                max(fizyka_p, chemia_p, biologia_p, informatyka_p, geografia_p),
                max(fizyka_p + fizyka_r * 1.5, chemia_p + chemia_r * 1.5,
                    biologia_p + biologia_r * 1.5, informatyka_p + informatyka_r * 1.5,
                    geografia_p + geografia_r * 1.5)
            )

        M = max(matematyka_r * 2.5, matematyka_p,
                matematyka_p + matematyka_r * 1.5)
        JO = max(angielski_p * 0.1, angielski_r * 0.25)
        JP = 0.1 * max(polski_p, polski_r)
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


def user_qualified(qualified_list, users, applications):
    for user in users:
        if user not in qualified_list:
            if user not in applications.user:
                return False
    return True


def sortApplications(applications):
    if len(applications) <= 1:
        return applications

    pivot_row = applications[len(applications) // 2]
    pivot_value = pivot_row[7]

    less = [row for row in applications if row[7] < pivot_value]
    equal = [row for row in applications if row[7] == pivot_value]
    greater = [row for row in applications if row[7] > pivot_value]

    return sortApplications(less, 1) + equal + sortApplications(greater, 1)


def ilosc_linii_w_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        ilosc_linii = sum(1 for linia in plik)
    return ilosc_linii


def zapisz_do_pliku(nazwa_pliku, tekst):
    with open(nazwa_pliku, 'a') as plik:
        plik.write(tekst + '\n')


def wyczysc_plik(nazwa_pliku):
    with open(nazwa_pliku, 'w') as plik:
        pass


def qualify_stacks(request):
    applications = Applications.objects.all()
    limits = Majors.objects.values('major', 'limit', flat=True)
    users = AuthUser.objects.values_list('username', flat=True).distinct()
    qualified = []
    compiting_applications = []
    stop_condition = user_qualified(qualified, users, applications)

    for kierunek in limits.major:
        nazwa_pliku = f'{kierunek}.txt'

    while stop_condition:
        for kierunek in limits.major:
            wyczysc_plik(f'{kierunek}.txt')
        for user in users:
            user_applications = applications.user.lications.user
            compiting_applications.append(
                sorted(applications, key=lambda x: x.preference)[0])

    sorted_applications = sortApplications(compiting_applications)

    for application in sorted_applications:
        miejsca = ilosc_linii_w_pliku(f'{application.major}.txt')
        app_major = application.major
        if miejsca < limits.app_major:
            zapisz_do_pliku(f'{application.major}.txt', application.user)
        compiting_applications.remove(application)


def find_row(table, val_to_find):
    found_row = None
    for row in table:
        if row[0] == val_to_find:
            return row


def qualify_sort(request):
    applications = Applications.objects.all().order_by('preference', 'score')
    limits = Majors.objects.values('major', 'limit', flat=True)
    for row in limits:
        row.append(None)
    qualified = []
    compiting_applications = []

    for kierunek in limits.major:
        nazwa_pliku = f'{kierunek}_sort.txt'

    for application in applications:
        if application.user not in qualified:
            app_major = application.major
            current_threshold = find_row(limits, app_major)
            if application.score > current_threshold:
                miejsca = ilosc_linii_w_pliku(f'{application.major}_sort.txt')
                if miejsca < limits.app_major:
                    zapisz_do_pliku(
                        f'{application.major}_sort.txt', application.user)
                else:
                    pass
