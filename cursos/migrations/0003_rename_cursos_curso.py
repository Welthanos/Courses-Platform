# Generated by Django 3.2.8 on 2021-10-08 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_rename_aulas_aula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
    ]
