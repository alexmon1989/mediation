# Generated by Django 4.2.4 on 2024-04-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0011_alter_educationalinstitution_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionaldirections',
            name='title',
            field=models.CharField(max_length=2048, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='professionaldirections',
            name='title_en',
            field=models.CharField(max_length=2048, null=True, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='professionaldirections',
            name='title_uk',
            field=models.CharField(max_length=2048, null=True, verbose_name='Назва'),
        ),
    ]
