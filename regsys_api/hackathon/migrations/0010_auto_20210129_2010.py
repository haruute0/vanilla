# Generated by Django 2.2.7 on 2021-01-29 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0009_auto_20210129_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='alergi_makanan',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='vegetarian_bool',
        ),
        migrations.DeleteModel(
            name='AnggotaTim',
        ),
    ]
