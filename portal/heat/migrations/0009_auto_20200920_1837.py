# Generated by Django 3.1.1 on 2020-09-20 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heat', '0008_auto_20200920_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcecharge',
            options={'ordering': ['time_record'], 'verbose_name': 'Расчёт ресурсов', 'verbose_name_plural': 'Расчёт ресурсов'},
        ),
    ]
