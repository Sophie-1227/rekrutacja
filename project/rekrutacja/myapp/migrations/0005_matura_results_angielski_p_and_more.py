# Generated by Django 4.2.7 on 2023-12-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_personal_data_pesel'),
    ]

    operations = [
        migrations.AddField(
            model_name='matura_results',
            name='angielski_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='angielski_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='biologia_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='biologia_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='chemia_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='chemia_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='fizyka_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='fizyka_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='geografia_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='geografia_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='informatyka_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='informatyka_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='matematyka_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='matematyka_r',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='polski_p',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='matura_results',
            name='polski_r',
            field=models.IntegerField(null=True),
        ),
    ]