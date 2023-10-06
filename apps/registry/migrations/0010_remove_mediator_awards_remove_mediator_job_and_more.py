# Generated by Django 4.2.4 on 2023-10-06 13:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0009_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediator',
            name='awards',
        ),
        migrations.RemoveField(
            model_name='mediator',
            name='job',
        ),
        migrations.RemoveField(
            model_name='mediator',
            name='job_experience',
        ),
        migrations.RemoveField(
            model_name='mediator',
            name='mediators_membership',
        ),
        migrations.RemoveField(
            model_name='mediator',
            name='other',
        ),
        migrations.RemoveField(
            model_name='mediator',
            name='price',
        ),
        migrations.AddField(
            model_name='mediator',
            name='additional_info',
            field=ckeditor.fields.RichTextField(blank=True, max_length=2048, null=True, verbose_name='Додаткова інформація'),
        ),
    ]
