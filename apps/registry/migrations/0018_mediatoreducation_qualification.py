# Generated by Django 4.2.4 on 2024-04-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0017_alter_mediatorprofessionaldirections_professional_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediatoreducation',
            name='qualification',
            field=models.CharField(blank=True, default='', verbose_name='Кваліфікація'),
        ),
    ]