# Generated by Django 4.2.4 on 2024-04-08 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifiers', '0010_educationalcourse_title_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationalinstitution',
            options={'ordering': ('title',), 'verbose_name': 'Освітній заклад', 'verbose_name_plural': 'Освітні заклади'},
        ),
    ]
