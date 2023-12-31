# Generated by Django 4.2.7 on 2023-12-14 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_subjects'),
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
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]
