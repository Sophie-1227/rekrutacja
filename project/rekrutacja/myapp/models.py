from django.db import models

# Create your models here.
class Personal_data(models.Model):
    TAK="Tak"
    NIE="Nie"
    tak_nie=[
        (TAK, "tak"),
        (NIE, "nie")
    ]
    KOBIETA="Kobieta"
    MEZCZYZNA = "Mężczyzna"
    INNA = "Inna"
    sex_choices =[
        (KOBIETA, "Kobieta"),
        (MEZCZYZNA, "Mężczyzna"),
        (INNA, "Inna")
    ]
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(length=9) #TODO add country code and template
    date_of_birth = models.DateField
    father_name = models.CharField(max_length=100)
    is_polish = models.CharField(max_length=3, choices=tak_nie, default=TAK)
    sex = models.CharField(max_length=9, choices=sex_choices)

class Adress(models.Model):
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6) #TODO: create template for anwsering with _ _ - _ _ _
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=4)

class High_school(models.Model):
    LICEUM_O = "Liceum Ogólnokształcące"
    LICEUM_P = "Liceum Profilowane"
    TECHNIKUM = "Technikum"
    BRANZOWA = "Branżowa Szkoła II Stopnia "
    School_type_choice = [
        (LICEUM_O, "Liceum Ogólnokształcące"),
        (LICEUM_P, "Liceum Profilowane"),
        (TECHNIKUM, "TECHNIKUM"),
        (BRANZOWA, "Branżowa Szkoła II Stopnia")
    ]
    school_type = models.CharField(max_length=100, choices=School_type_choice)
    school_name = models.CharField(max_length=200)
    school_country = models.CharField(max_length=100)
    school_city = models.CharField(max_length=100)

class Documents_matura(models.Model):
    exam_type = models.CharField(max_length=100) # TODO: add choices
    exam_year = models.IntegerField(length=4)
    exam_number = models.CharField(max_length=13)
    exam_issuer = models.CharField(max_length=100)
    exam_date = models.DateField
    exam_city = models.CharField(max_length=100)
    exam_country = models.CharField(max_length=100)

class Documents_achivment(models.Model):
    achivment_type= models.CharField(max_length=100) # TODO: add choices
    achivment_result= models.CharField(max_length=50) # TODO: add choices
    achivment_year= models.IntegerField(length=4)
    achivment_issuer = models.CharField(max_length=100)
    achivment_city = models.CharField(max_length=100)
    achivment_country = models.CharField(max_length=100)

class Documents_dyploma(models.Model):
    dyploma_type= models.CharField(max_length=100) # TODO: add choices
    dyploma_result= models.CharField(max_length=3) # TODO: add choices
    dyploma_avg= models.DecimalField(max_length=5)
    dyploma_year= models.IntegerField(length=4)
    dyploma_issuer = models.CharField(max_length=100)
    dyploma_city = models.CharField(max_length=100)
    dyploma_country = models.CharField(max_length=100)


class Matura_results(models.Model):
    polski_p = models.IntegerField(max_length=3)
    polski_r = models.IntegerField(max_length=3)
    matematyka_p = models.IntegerField(max_length=3)
    matematyka_r = models.IntegerField(max_length=3)
    angielski_p = models.IntegerField(max_length=3)
    angielski_r = models.IntegerField(max_length=3)
    fizyka_p = models.IntegerField(max_length=3)
    fizyka_r = models.IntegerField(max_length=3)
    chemia_p = models.IntegerField(max_length=3)
    chemia_r = models.IntegerField(max_length=3)
    geografia_p = models.IntegerField(max_length=3)
    geografia_r = models.IntegerField(max_length=3)
    biologia_p = models.IntegerField(max_length=3)
    biologia_r = models.IntegerField(max_length=3)
    informatyka_p = models.IntegerField(max_length=3)
    informatyka_r = models.IntegerField(max_length=3)

# class Preferences(models.Model): #redundancja -> widok?
#     preference1 = models.CharField(max_length=3)
#     preference2 = models.CharField(max_length=3)
#     preference3 = models.CharField(max_length=3)
#     preference4 = models.CharField(max_length=3)
#     preference5 = models.CharField(max_length=3)
#     preference6 = models.CharField(max_length=3)

class Applications(models.Model):
    preference = models.IntegerField(max_length=1, max=6)
    faculty = models.CharField(length=3) # TODO: add choices / automation based on major
    major = models.CharField(length=3)
    tour = models.IntegerField(length=1, max=6)
    is_active = models.BooleanField
    is_condition = models.BooleanField
    score = models.IntegerField(max_length=3)
    is_paid = models.BooleanField
    is_qualified = models.BooleanField
    are_documents = models.BooleanField
    decision = models.BooleanField