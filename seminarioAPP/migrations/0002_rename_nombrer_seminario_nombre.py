# Generated by Django 4.1 on 2022-12-16 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminarioAPP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seminario',
            old_name='nombreR',
            new_name='nombre',
        ),
    ]
