# Generated by Django 4.2.4 on 2023-08-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0002_specialization_alter_speciality_options_and_more'),
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediator',
            name='specializations',
            field=models.ManyToManyField(blank=True, to='classifiers.specialization', verbose_name='Спеціалізація'),
        ),
    ]
