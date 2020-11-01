from django.db import models


class Home(models.Model):
    """Таблица с перечнем адресов домов которые
    на управлении.
    """
    city = models.CharField("Город",
                            max_length=100)
    adress = models.CharField("Адрес", max_length=100)
    home_number = models.IntegerField("Номер дома")
    home_sub_number = models.CharField("Корпус",
                                       max_length=2,
                                       blank=True,
                                       default=0,
                                       help_text="Если отсутствует, \
                                       ставьте ноль")

    class Meta:
        ordering = ["adress", "home_number"]
        verbose_name = "Адрес дома"
        verbose_name_plural = "Адреса домов"
        unique_together = ('adress', 'home_number', 'home_sub_number')

    def __str__(self):
        # определяем наличие или отсутствие корпуса в адресе
        if self.home_sub_number == "0":
            return f"{self.adress} {self.home_number}"
        else:
            return f"{self.adress} {self.home_number} корп. \
                {self.home_sub_number}"

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.adress)))


class AbstractMain(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)

    class Meta:
        abstract = True


class HomeApartment(AbstractMain,
                    models.Model):
    """Таблица со списком жилых и нежилых помещений в доме.

    """
    APARTMENTS = [
        ("residential", "Жилое"),
        ("non-residential", "Нежилое")
    ]
    number = models.IntegerField("Номер помещения")
    apartment_type = models.CharField("Тип помещения", max_length=15,
                                      choices=APARTMENTS,
                                      default="residential")

    class Meta:
        ordering = ["home", "number"]
        verbose_name = "Перечень помещений"
        verbose_name_plural = "Перечень помещений"
        unique_together = ('home', 'number')

    def __str__(self):
        if self.apartment_type == "residential":
            return "".join((str(self.number), " кв."))
        else:
            return "".join((str(self.number), " пом."))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), "-", str(self.number)))


class HomeTechParametrs(AbstractMain,
                        models.Model):
    """Таблица с техническими параметрами дома.

        Сокращения:
            mop - места общего пользования
    """
    ELEVATORS = [
        ("YES", "Есть"),
        ("NO", "Нет")
    ]

    year_building = models.IntegerField("Год ввода в эксплуатацию",
                                        help_text="")
    entrances = models.IntegerField("Количество подъездов",
                                    help_text="")
    elevators = models.CharField("Лифты",
                                 max_length=4,
                                 choices=ELEVATORS,
                                 default="NO",
                                 help_text="Наличие лифтов")
    floor = models.IntegerField("Этажей",
                                help_text="Общее количество этажей")
    living_room = models.IntegerField("Количество жилых помещений",
                                      help_text="")
    non_living_room = models.IntegerField("Количество нежилых помещений",
                                          help_text="")
    square_full = models.DecimalField("Общая площадь всех помещений",
                                      max_digits=6,
                                      decimal_places=2,
                                      help_text="метры квадратные")
    square_living = models.DecimalField("Площадь жилых помещений",
                                        max_digits=6,
                                        decimal_places=2,
                                        help_text="метры квадратные")
    square_non_living = models.DecimalField("Площадь мест общего пользования",
                                            max_digits=6,
                                            decimal_places=2,
                                            help_text="метры квадратные")
    square_cleaning = models.DecimalField("Площадь мест общего пользования",
                                          max_digits=6,
                                          decimal_places=2,
                                          help_text="метры квадратные")
    square_mop = models.DecimalField("Площадь мест общего пользования",
                                     max_digits=6,
                                     decimal_places=2,
                                     help_text="метры квадратные")
    square_land_area = models.DecimalField("Площадь земельного участка",
                                           max_digits=6,
                                           decimal_places=2,
                                           help_text="")
    land_reg_number = models.CharField("Кадастровый номер земельного участка",
                                       help_text="")

    class Meta:
        ordering = ["home"]
        verbose_name = "Технические параметры дома"
        verbose_name_plural = "Технических параметров домов"
        unique_together = ('home')

    def __str__(self):
        return "".join((str(self.home), ": HomeTechParametrs"))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.home)))


class HomeManagmentParameters(AbstractMain,
                              models.Model):
    """Параметры управления.
    """
    contract_date = models.DateField("Дата заключения договора",
                                     help_text="")
    start_date = models.DateField("Дата начала управления",
                                  help_text="")
    end_date = models.DateField("Планируемая дата окончания управления",
                                help_text="")

    class Meta:
        ordering = ["home"]
        verbose_name = "Параметры управления"
        verbose_name_plural = "Парметров управления"
        unique_together = ('home')

    def __str__(self):
        return "".join((str(self.home), ": HomeManagmentParameters"))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.home)))


class HomeNormativeParameters(AbstractMain,
                              models.Model):
    """Таблица нормативов.
    """
    norm_hot_water = models.DecimalField("Норматив горячего водоснабжения",
                                         max_digits=3,
                                         decimal_places=2,
                                         help_text="тонн на метр квадратный")
    norm_cold_water = models.DecimalField("Норматив холодного водоснабжения",
                                          max_digits=3,
                                          decimal_places=2,
                                          help_text="тонн на метр квадратный")
    norm_preheating = models.DecimalField("Норматив на подогрев",
                                          max_digits=3,
                                          decimal_places=2,
                                          help_text="Гкал на тонну квадратный")
    norm_heating = models.DecimalField("Норматив на отопление",
                                       max_digits=5,
                                       decimal_places=4,
                                       help_text="Гкал на метр квадратный")
    norm_wastewater = models.DecimalField("Норматив водоотведения",
                                          max_digits=5,
                                          decimal_places=4,
                                          help_text="тонн на метр квадратный")

    class Meta:
        ordering = ["home"]
        verbose_name = "Нормативы"
        verbose_name_plural = "Нормативов"
        unique_together = ('home')

    def __str__(self):
        return "".join((str(self.home), ": HomeNormativeParameters"))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.home)))


class HomeEconomicParameters(models.Model):
    tarif_hot_water = models.DecimalField("Тариф, на ХВ для ГВС",
                                          max_digits=5,
                                          decimal_places=2,
                                          help_text="рублей за тонну")
    tarif_preheating = models.DecimalField("Тариф, на Гкал для ГВС",
                                           max_digits=5,
                                           decimal_places=2,
                                           help_text="рублей за Гкалорию")
    tarif_heating = models.DecimalField("Тариф, на Гкал для отопления",
                                        max_digits=5,
                                        decimal_places=2,
                                        help_text="рублей за Гкалорию")
    tarif_cold_water = models.DecimalField("Тариф, на ХВС",
                                           max_digits=5,
                                           decimal_places=2,
                                           help_text="рублей за тонну")
    tarif_wastewater = models.DecimalField("Тариф, на Водоотведение",
                                           max_digits=5,
                                           decimal_places=2,
                                           help_text="рублей за тонну")
    nalog = models.DecimalField("Налог",
                                max_digits=3,
                                decimal_places=1,
                                default=20)

    class Meta:
        ordering = ["home"]
        verbose_name = "Тарифы"
        verbose_name_plural = "Тарифов"
        unique_together = ('home')

    def __str__(self):
        return "".join((str(self.home), ": HomeEconomicParameters"))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.home)))
