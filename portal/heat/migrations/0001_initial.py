# Generated by Django 3.1.1 on 2020-09-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250, verbose_name='Город')),
                ('adress', models.CharField(max_length=250, verbose_name='Адрес')),
                ('home_number', models.IntegerField(verbose_name='Номер дома')),
                ('home_sub_number', models.CharField(blank=True, default=0, help_text='Если отсутствует,                                        ставьте ноль', max_length=2, verbose_name='Корпус')),
            ],
            options={
                'verbose_name': 'home',
                'verbose_name_plural': 'home',
                'ordering': ['adress', 'home_number'],
            },
        ),
        migrations.CreateModel(
            name='ResourceCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Обновлено')),
                ('time_record', models.DateField(verbose_name='Дата')),
                ('normative', models.DecimalField(decimal_places=3, help_text='тонн на метр квадратный', max_digits=6, verbose_name='Норматив')),
                ('tarif', models.DecimalField(decimal_places=2, help_text='рублей за тонну', max_digits=5, verbose_name='Тариф')),
                ('nalog', models.IntegerField(default=0, verbose_name='Налог')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'resource charge',
                'verbose_name_plural': 'resource charge',
                'ordering': ['time_record'],
            },
        ),
        migrations.CreateModel(
            name='HomeApartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер помещения')),
                ('apartment_type', models.CharField(choices=[('residential', 'Жилое'), ('non-residential', 'Нежилое')], default='residential', max_length=15, verbose_name='Тип помещения')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'home apartment',
                'verbose_name_plural': 'home apartment',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='ConsumptionODPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('cold_water', 'Холодная вода'), ('hot_water', 'Горячая вода'), ('heating', 'Отопление'), ('drainage', 'Водоотведение'), ('electricity', 'Электричество')], default='heating', max_length=15, verbose_name='Тип коммунального ресурса')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Обновлено')),
                ('time_record', models.DateField(verbose_name='Дата')),
                ('temp1', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='T1')),
                ('temp2', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='T2')),
                ('G1', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='G1')),
                ('G2', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='G2')),
                ('work_time', models.IntegerField(verbose_name='Время нормальной работы')),
                ('idle_time', models.IntegerField(verbose_name='Время простоя')),
                ('Q1', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Q1')),
                ('M1', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='M1')),
                ('M2', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='M1')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'consumption odpu',
                'verbose_name_plural': 'consumption odpu',
                'ordering': ['time_record'],
            },
        ),
        migrations.CreateModel(
            name='HomeParametrs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MOP', models.DecimalField(decimal_places=2, help_text='метры квадратные', max_digits=5, verbose_name='Площадь мест общего пользования')),
                ('norm_cold_water', models.DecimalField(decimal_places=2, help_text='тонн на метр квадратный', max_digits=3, verbose_name='Норматив горячего водоснабжения')),
                ('norm_hot_water', models.DecimalField(decimal_places=2, help_text='тонн на метр квадратный', max_digits=3, verbose_name='Норматив холодного водоснабжения')),
                ('nor_heating', models.DecimalField(decimal_places=4, help_text='Гкал на метр квадратный', max_digits=5, verbose_name='Норматив отопления или подогрев')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'home parametrs',
                'verbose_name_plural': 'home parametrs',
                'order_with_respect_to': 'home',
            },
        ),
        migrations.CreateModel(
            name='ConsumptionRSO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Обновлено')),
                ('time_record', models.DateField(verbose_name='Дата')),
                ('ODPU_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Расход по ОДПУ')),
                ('ODPU_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Расход по ОДПУ')),
                ('IPU_RP_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Расход по ИПУ (жилые пом.)')),
                ('IPU_RP_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Расход по ИПУ (жилые пом.)')),
                ('IPU_nonRP_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Расхо по ИПУ (нежил. пом.)')),
                ('IPU_nonRP_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Расход по ИПУ (неж. пом)')),
                ('ODN_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Расход по ОДН')),
                ('ODN_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Расход по ОДН')),
                ('negative_ODN_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Отрицательный ОДН')),
                ('negative_ODN_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Отрицательный ОДН')),
                ('result_ODN_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='Итоговый ОДН')),
                ('result_ODN_calories', models.DecimalField(decimal_places=5, help_text='Гкал', max_digits=9, verbose_name='Итоговый ОДН')),
                ('payable_ODN_mass', models.DecimalField(decimal_places=3, help_text='тонн', max_digits=8, verbose_name='ОДН к начислению')),
                ('payable_ODN_calories', models.DecimalField(decimal_places=5, help_text='тонн', max_digits=9, verbose_name='ОДН к начислению')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'consumption rso',
                'verbose_name_plural': 'consumption rso',
                'order_with_respect_to': 'home',
            },
        ),
        migrations.CreateModel(
            name='ConsumptionIPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Обновлено')),
                ('time_record', models.DateField(verbose_name='Дата')),
                ('IPU_mass', models.DecimalField(decimal_places=3, help_text='тонны', max_digits=7, verbose_name='Расход по ИПУ')),
                ('IPU_calories', models.DecimalField(decimal_places=6, help_text='Гкал', max_digits=8, verbose_name='Расход по ИПУ')),
                ('recalculation_mass', models.DecimalField(decimal_places=3, help_text='тонны', max_digits=7, verbose_name='Перерасчёт')),
                ('recalculation_calories', models.DecimalField(decimal_places=6, help_text='Гкал', max_digits=8, verbose_name='Перерасчёт')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.homeapartment')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heat.home')),
            ],
            options={
                'verbose_name': 'consumption IPU',
                'verbose_name_plural': 'consumption IPU',
                'order_with_respect_to': 'apartment',
            },
        ),
    ]
