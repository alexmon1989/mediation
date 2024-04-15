# Generated by Django 4.2.4 on 2024-04-11 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0011_alter_educationalinstitution_options'),
        ('registry', '0014_mediator_additional_info_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediator',
            name='professional_directions',
        ),
        migrations.AlterField(
            model_name='mediator',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='По-батькові'),
        ),
        migrations.CreateModel(
            name='MediatorProfessionalDirections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('weight', models.PositiveIntegerField(default=0)),
                ('mediator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registry.mediator')),
                ('professional_direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifiers.professionaldirections')),
            ],
            options={
                'verbose_name': 'Професійний напрямок медіатора',
                'verbose_name_plural': 'Професійні напрямки медіатора',
                'db_table': 'mediators_professional_directions',
            },
        ),
    ]
