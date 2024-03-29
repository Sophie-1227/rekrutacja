from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
# from . import signals
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
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
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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
    TAK = "Tak"
    NIE = "Nie"
    tak_nie = [
        (TAK, "tak"),
        (NIE, "nie")
    ]
    KOBIETA = "Kobieta"
    MEZCZYZNA = "Mężczyzna"
    INNA = "Inna"
    sex_choices = [
        (KOBIETA, "Kobieta"),
        (MEZCZYZNA, "Mężczyzna"),
        (INNA, "Inna")
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    pesel = models.PositiveIntegerField(unique=True, null=True)
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    # TODO add country code and template
    phone = models.PositiveIntegerField(null=True)
    father_name = models.CharField(max_length=100, null=True)
    is_polish = models.CharField(max_length=3, choices=tak_nie, default=TAK)
    sex = models.CharField(max_length=9, choices=sex_choices, null=True)


class Adress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    country = models.CharField(max_length=100, null=True)
    # TODO: create template for anwsering with _ _ - _ _ _
    postal_code = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    building_number = models.CharField(max_length=10, null=True)
    apartment_number = models.CharField(max_length=4, null=True)


class High_school(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    IB = "Matura IB"
    Europejska = "Matura Europejska"
    Dwujezyczna = "Polska matura dwujęzyczna"
    Zagraniczna = "Matura zagranczna"
    Stara25 = "Polska stara matura (skala ocen 2-5)"
    Stara16 = "Polska stara matura (skala ocen 1-6)"
    Nowa = "Polska nowa matura"
    Exam_types = [
        (IB, "Matura IB"),
        (Europejska, "Matura Europejska"),
        (Dwujezyczna, "Polska matura dwujęzyczna"),
        (Zagraniczna, "Matura zagranczna"),
        (Stara25, "Polska stara matura (skala ocen 2-5)"),
        (Stara16, "Polska stara matura (skala ocen 1-6)"),
        (Nowa, "Polska nowa matura"),
    ]
    exam_type = models.CharField(max_length=100)
    exam_year = models.IntegerField(null=True)
    exam_number = models.CharField(max_length=13)
    exam_issuer = models.CharField(max_length=100)
    exam_city = models.CharField(max_length=100)
    exam_country = models.CharField(max_length=100)


class Documents_achivment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    achivment_type = models.CharField(max_length=100)  # TODO: add choices
    # TODO: add choices #TODO change to boolean isaccepted avaible for admin only
    achivment_result = models.CharField(max_length=50)
    achivment_year = models.IntegerField(null=True)
    achivment_issuer = models.CharField(max_length=100)
    achivment_city = models.CharField(max_length=100)
    achivment_country = models.CharField(max_length=100)


class Documents_dyploma(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    dyploma_type = models.CharField(max_length=100)  # TODO: add choices
    dyploma_result = models.CharField(max_length=3)  # TODO: add choices
    dyploma_avg = models.DecimalField(
        decimal_places=3, max_digits=5, null=True)
    dyploma_year = models.IntegerField(null=True)
    dyploma_issuer = models.CharField(max_length=100)
    dyploma_city = models.CharField(max_length=100)
    dyploma_country = models.CharField(max_length=100)


class Matura_results(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    polski_p = models.IntegerField(null=True)
    polski_r = models.IntegerField(null=True)
    matematyka_p = models.IntegerField(null=True)
    matematyka_r = models.IntegerField(null=True)
    angielski_p = models.IntegerField(null=True)
    angielski_r = models.IntegerField(null=True)
    fizyka_p = models.IntegerField(null=True)
    fizyka_r = models.IntegerField(null=True)
    chemia_p = models.IntegerField(null=True)
    chemia_r = models.IntegerField(null=True)
    geografia_p = models.IntegerField(null=True)
    geografia_r = models.IntegerField(null=True)
    biologia_p = models.IntegerField(null=True)
    biologia_r = models.IntegerField(null=True)
    informatyka_p = models.IntegerField(null=True)
    informatyka_r = models.IntegerField(null=True)


class Applications(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    preference = models.IntegerField(null=True)
    # TODO: add choices / automation based on major
    faculty = models.CharField(max_length=3)
    major = models.CharField(max_length=3)
    tour = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    is_condition = models.BooleanField(default=False)
    score = models.FloatField(null=True)
    is_paid = models.BooleanField(default=False)
    is_qualified = models.BooleanField(null=True)
    are_documents = models.BooleanField(default=False)
    decision = models.BooleanField(null=True)


class Majors(models.Model):
    major = models.CharField(max_length=100)
    chemia = models.BooleanField(default=False)
    informatyka = models.BooleanField(default=False)
    biologia = models.BooleanField(default=False)
    geografia = models.BooleanField(default=False)
    limit = models.IntegerField(null=True)
