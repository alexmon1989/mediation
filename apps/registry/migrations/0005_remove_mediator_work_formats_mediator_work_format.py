# Generated by Django 4.2.4 on 2023-08-15 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0003_professionaldirections'),
        ('registry', '0004_remove_mediator_professional_directions_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediator',
            name='work_formats',
        ),
        migrations.AddField(
            model_name='mediator',
            name='work_format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classifiers.workformat', verbose_name='Формат роботи'),
        ),
    ]
