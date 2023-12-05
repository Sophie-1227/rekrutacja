from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    pesel = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.PositiveIntegerField() #TODO add country code and template
    # date_of_birth = models.DateField()
    father_name = models.CharField(max_length=100)
    is_polish = models.CharField(max_length=3, choices=tak_nie, default=TAK)
    sex = models.CharField(max_length=9, choices=sex_choices)

class Adress(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6) #TODO: create template for anwsering with _ _ - _ _ _
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building_number = models.CharField(max_length=10)
    apartment_number = models.CharField(max_length=4)

class High_school(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
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
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=100) # TODO: add choices
    exam_year = models.IntegerField
    exam_number = models.CharField(max_length=13)
    exam_issuer = models.CharField(max_length=100)
    exam_date = models.DateField
    exam_city = models.CharField(max_length=100)
    exam_country = models.CharField(max_length=100)

class Documents_achivment(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    achivment_type= models.CharField(max_length=100) # TODO: add choices
    achivment_result= models.CharField(max_length=50) # TODO: add choices
    achivment_year= models.IntegerField
    achivment_issuer = models.CharField(max_length=100)
    achivment_city = models.CharField(max_length=100)
    achivment_country = models.CharField(max_length=100)

class Documents_dyploma(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    dyploma_type= models.CharField(max_length=100) # TODO: add choices
    dyploma_result= models.CharField(max_length=3) # TODO: add choices
    dyploma_avg= models.DecimalField(decimal_places=3, max_digits=5)
    dyploma_year= models.IntegerField
    dyploma_issuer = models.CharField(max_length=100)
    dyploma_city = models.CharField(max_length=100)
    dyploma_country = models.CharField(max_length=100)


class Matura_results(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    polski_p = models.IntegerField
    polski_r = models.IntegerField
    matematyka_p = models.IntegerField
    matematyka_r = models.IntegerField
    angielski_p = models.IntegerField
    angielski_r = models.IntegerField
    fizyka_p = models.IntegerField
    fizyka_r = models.IntegerField
    chemia_p = models.IntegerField
    chemia_r = models.IntegerField
    geografia_p = models.IntegerField
    geografia_r = models.IntegerField
    biologia_p = models.IntegerField
    biologia_r = models.IntegerField
    informatyka_p = models.IntegerField
    informatyka_r = models.IntegerField

# class Preferences(models.Model): #redundancja -> widok?
#     ID = models.ForeignKey(auth.user, related_name=id, unique=True, notnull=True)
#     preference1 = models.CharField(max_length=3)
#     preference2 = models.CharField(max_length=3)
#     preference3 = models.CharField(max_length=3)
#     preference4 = models.CharField(max_length=3)
#     preference5 = models.CharField(max_length=3)
#     preference6 = models.CharField(max_length=3)

class Applications(models.Model):
  #  ID = models.ForeignKey(User, related_name=id, on_delete=models.CASCADE)
    preference = models.IntegerField
    faculty = models.CharField(max_length=3) # TODO: add choices / automation based on major
    major = models.CharField(max_length=3)
    tour = models.IntegerField
    is_active = models.BooleanField
    is_condition = models.BooleanField
    score = models.IntegerField
    is_paid = models.BooleanField
    is_qualified = models.BooleanField
    are_documents = models.BooleanField
    decision = models.BooleanField