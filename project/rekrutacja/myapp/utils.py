from django.http import JsonResponse
from myapp.models import Applications, Matura_results, Majors, Documents_matura, AuthUser
from django.shortcuts import get_object_or_404
from django.db.models import Max


# calculating points for each application


def calculate_score(request):
    applications = Applications.objects.all()

    for application in applications:
        user = application.user
        major = application.major
        PD_major = Majors.objects.filter(major=major).first()
        exam_type = Documents_matura.objects.filter(
            user=user).values('exam_type')
        wyniki_matury = Matura_results.objects.filter(user=user)
        wyniki_matury_list = []
        for result in wyniki_matury:
            result_data = {
                'polski_p': result.polski_p or 0,
                'polski_r': result.polski_r or 0,
                'matematyka_p': result.matematyka_p or 0,
                'matematyka_r': result.matematyka_r or 0,
                'angielski_p': result.angielski_p or 0,
                'angielski_r': result.angielski_r or 0,
                'fizyka_p': result.fizyka_p or 0,
                'fizyka_r': result.fizyka_r or 0,
                'chemia_p': result.chemia_p or 0,
                'chemia_r': result.chemia_r or 0,
                'geografia_p': result.geografia_p or 0,
                'geografia_r': result.geografia_r or 0,
                'biologia_p': result.biologia_p or 0,
                'biologia_r': result.biologia_r or 0,
                'informatyka_p': result.informatyka_p or 0,
                'informatyka_r': result.informatyka_r or 0,
            }
            wyniki_matury_list.append(result_data)
        is_condition = False
        PD = 0
        if exam_type == 'maturaIB':
            # Implementacja algorytmu dla matury IB
            for wynik in wyniki_matury_list:
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

        # Print the queryset
        print(wyniki_matury_list)

        polski_p = wyniki_matury_list[0]['polski_p']
        angielski_p = wyniki_matury_list[0]['angielski_p']
        matematyka_p = wyniki_matury_list[0]['matematyka_p']
        polski_r = wyniki_matury_list[0]['polski_r']
        angielski_r = wyniki_matury_list[0]['angielski_r']
        matematyka_r = wyniki_matury_list[0]['matematyka_r']

        if polski_p >= 30 and angielski_p >= 30 and matematyka_p >= 30:
            if exam_type == 'nowaMatura':
                fizyka = wyniki_matury_list[0]['fizyka_r']
                chemia = wyniki_matury_list[0]['chemia_r'] * \
                    int(PD_major.chemia)
                biologia = wyniki_matury_list[0]['biologia_r'] * \
                    int(PD_major.biologia)
                informatyka = wyniki_matury_list[0]['informatyka_r'] * \
                    int(PD_major.informatyka)
                geografia = wyniki_matury_list[0]['geografia_r'] * \
                    int(PD_major.geografia)
                PD = 2.5 * max(fizyka, chemia, biologia,
                               informatyka, geografia)
            else:
                fizyka_r = wyniki_matury_list[0]['fizyka_r']
                chemia_r = wyniki_matury_list[0]['chemia_r'] * \
                    int(PD_major.chemia)
                biologia_r = wyniki_matury_list[0]['biologia_r'] * \
                    int(PD_major.biologia)
                informatyka_r = wyniki_matury_list[0]['informatyka_r'] * \
                    int(PD_major.informatyka)
                geografia_r = wyniki_matury_list[0]['geografia_r'] * \
                    int(PD_major.geografia)

                fizyka_p = wyniki_matury_list[0]['fizyka_p']
                chemia_p = wyniki_matury_list[0]['chemia_p'] * \
                    int(PD_major.chemia)
                biologia_p = wyniki_matury_list[0]['biologia_p'] * \
                    int(PD_major.biologia)
                informatyka_p = wyniki_matury_list[0]['informatyka_p'] * \
                    int(PD_major.informatyka)
                geografia_p = wyniki_matury_list[0]['geografia_p'] * \
                    int(PD_major.geografia)

                PD = max(
                    2.5 * max(fizyka_r, chemia_r, biologia_r,
                              informatyka_r, geografia_r),
                    max(fizyka_p, chemia_p, biologia_p,
                        informatyka_p, geografia_p),
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

        print(score, "score")

        # Wynik w formie JSON
        result = {
            'score': score,
            'is_condition': is_condition,
        }
        return JsonResponse(result)


def user_qualified(qualified_list, users, applications):
    sum = 0
    for user in users:
        if user not in qualified_list:
            if user not in applications.user:
                sum += 1
        else:
            sum += 1
    return sum >= len(users)


def sortApplications(applications):
    if len(applications) <= 1:
        return applications

    pivot_row = applications[len(applications) // 2]
    pivot_value = pivot_row[7]

    less = [row for row in applications if row[7] < pivot_value]
    equal = [row for row in applications if row[7] == pivot_value]
    greater = [row for row in applications if row[7] > pivot_value]

    return sortApplications(less, 1) + equal + sortApplications(greater, 1)


def ilosc_linii_w_pliku(file_name):
    with open(file_name, 'r') as plik:
        ilosc_linii = sum(1 for linia in plik)
    return ilosc_linii


def zapisz_do_pliku(file_name, tekst):
    with open(file_name, 'a') as plik:
        plik.write(tekst + '\n')


def wyczysc_plik(file_name):
    with open(file_name, 'w') as plik:
        pass


def qualify_stacks(request):
    applications = Applications.objects.all()
    limits = Majors.objects.values('major', 'limit', flat=True)
    users = AuthUser.objects.values_list('username', flat=True).distinct()
    qualified = []
    compiting_applications = []
    stop_condition = user_qualified(qualified, users, applications)

    for kierunek in limits.major:
        file_name = f'{kierunek}.txt'

    while stop_condition:
        for kierunek in limits.major:
            wyczysc_plik(f'{kierunek}.txt')
        for user in users:
            user_applications = applications.user
            compiting_applications.append(
                sorted(user_applications, key=lambda x: x.preference)[0])

        sorted_applications = sortApplications(compiting_applications)

        for application in sorted_applications:
            miejsca = ilosc_linii_w_pliku(f'{application.major}.txt')
            app_major = application.major
            if miejsca < limits.app_major:
                zapisz_do_pliku(f'{application.major}.txt', application.user)
            compiting_applications.remove(application)
        stop_condition = user_qualified(qualified, users, applications)


def find_row(table, val_to_find):
    found_row = None
    for row in table:
        if row[0] == val_to_find:
            return row


def find_preference(table, val_to_find):
    found_row = None
    for row in table:
        if row[1] == val_to_find:
            return row


def file_to_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def write_list_to_file(file_name, list):
    with open(file_name, 'w') as file:
        for row in list:
            file.write('\t'.join(map(str, row)) + '\n')


def qualify_sort(request):
    applications = Applications.objects.all().order_by('preference')
    limits = Majors.objects.values('major', 'limit', flat=True)
    for row in limits:
        row.append(None)
    qualified = []
    compiting_applications = []

    for kierunek in limits.major:
        file_name = f'{kierunek}_sort.txt'

    i = 0
    while i < len(applications):
        # for application in applications:
        application = applications[i]
        if application.user not in qualified:
            app_major = application.major
            current_threshold = find_row(limits, app_major)
            if application.score > current_threshold:
                miejsca = ilosc_linii_w_pliku(f'{application.major}_sort.txt')
                if miejsca < limits.app_major:
                    zapisz_do_pliku(
                        f'{application.major}_sort.txt', application)
                else:
                    lista = file_to_list(f'{application.major}_sort.txt')
                    lista.append(application)
                    sortedLista = sortApplications(lista)
                    disqualified = sortedLista[-1]
                    sortedLista.pop(-1)
                    preference = disqualified[1] - 1
                    loop_preference = find_preference(applications, preference)
                    i = loop_preference
