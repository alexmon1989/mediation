# Generated by Django 4.2.4 on 2023-08-16 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0003_professionaldirections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalcourse',
            name='educational_institution',
        ),
    ]
