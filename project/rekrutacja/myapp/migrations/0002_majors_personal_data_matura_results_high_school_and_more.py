# Generated by Django 4.2.7 on 2024-01-28 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('chemia', models.BooleanField(default=False)),
                ('informatyka', models.BooleanField(default=False)),
                ('biologia', models.BooleanField(default=False)),
                ('geografia', models.BooleanField(default=False)),
                ('limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pesel', models.PositiveIntegerField(null=True, unique=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('second_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.PositiveIntegerField(null=True)),
                ('father_name', models.CharField(max_length=100, null=True)),
                ('is_polish', models.CharField(choices=[('Tak', 'tak'), ('Nie', 'nie')], default='Tak', max_length=3)),
                ('sex', models.CharField(choices=[('Kobieta', 'Kobieta'), ('Mężczyzna', 'Mężczyzna'), ('Inna', 'Inna')], max_length=9, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matura_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polski_p', models.IntegerField(null=True)),
                ('polski_r', models.IntegerField(null=True)),
                ('matematyka_p', models.IntegerField(null=True)),
                ('matematyka_r', models.IntegerField(null=True)),
                ('angielski_p', models.IntegerField(null=True)),
                ('angielski_r', models.IntegerField(null=True)),
                ('fizyka_p', models.IntegerField(null=True)),
                ('fizyka_r', models.IntegerField(null=True)),
                ('chemia_p', models.IntegerField(null=True)),
                ('chemia_r', models.IntegerField(null=True)),
                ('geografia_p', models.IntegerField(null=True)),
                ('geografia_r', models.IntegerField(null=True)),
                ('biologia_p', models.IntegerField(null=True)),
                ('biologia_r', models.IntegerField(null=True)),
                ('informatyka_p', models.IntegerField(null=True)),
                ('informatyka_r', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='High_school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_type', models.CharField(choices=[('Liceum Ogólnokształcące', 'Liceum Ogólnokształcące'), ('Liceum Profilowane', 'Liceum Profilowane'), ('Technikum', 'TECHNIKUM'), ('Branżowa Szkoła II Stopnia ', 'Branżowa Szkoła II Stopnia')], max_length=100)),
                ('school_name', models.CharField(max_length=200)),
                ('school_country', models.CharField(max_length=100)),
                ('school_city', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents_matura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(max_length=100)),
                ('exam_year', models.IntegerField(null=True)),
                ('exam_number', models.CharField(max_length=13)),
                ('exam_issuer', models.CharField(max_length=100)),
                ('exam_city', models.CharField(max_length=100)),
                ('exam_country', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents_dyploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dyploma_type', models.CharField(max_length=100)),
                ('dyploma_result', models.CharField(max_length=3)),
                ('dyploma_avg', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('dyploma_year', models.IntegerField(null=True)),
                ('dyploma_issuer', models.CharField(max_length=100)),
                ('dyploma_city', models.CharField(max_length=100)),
                ('dyploma_country', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents_achivment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achivment_type', models.CharField(max_length=100)),
                ('achivment_result', models.CharField(max_length=50)),
                ('achivment_year', models.IntegerField(null=True)),
                ('achivment_issuer', models.CharField(max_length=100)),
                ('achivment_city', models.CharField(max_length=100)),
                ('achivment_country', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.IntegerField(null=True)),
                ('faculty', models.CharField(max_length=3)),
                ('major', models.CharField(max_length=3)),
                ('tour', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_condition', models.BooleanField(default=False)),
                ('score', models.FloatField(null=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_qualified', models.BooleanField(null=True)),
                ('are_documents', models.BooleanField(default=False)),
                ('decision', models.BooleanField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=6, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('building_number', models.CharField(max_length=10, null=True)),
                ('apartment_number', models.CharField(max_length=4, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
