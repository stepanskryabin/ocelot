from django.db import models


class Home(models.Model):
    """Таблица с перечнем адресов домов которые
    на управлении.

    """
    city = models.CharField("Город", max_length=100)
    adress = models.CharField("Адрес", max_length=100)
    home_number = models.IntegerField("Номер дома")
    home_sub_number = models.CharField("Корпус", max_length=2,
                                       blank=True, default=0,
                                       help_text="Если отсутствует, \
                                       ставьте ноль")

    class Meta:
        ordering = ["adress", "home_number"]
        verbose_name = "Адрес дома"
        verbose_name_plural = "Адреса домов"
        unique_together = ('adress', 'home_number', 'home_sub_number')

    def __str__(self):
        if self.home_sub_number == "0":
            return f"{self.adress} {self.home_number}"
        else:
            return f"{self.adress} {self.home_number} корп. \
                {self.home_sub_number}"

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ", str(self.adress)))


class HomeApartment(models.Model):
    """Таблица со списком жилых и нежилых помещений в доме.

    """
    APARTMENTS = [
        ("residential", "Жилое"),
        ("non-residential", "Нежилое")
    ]

    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
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


class HomeParametrs(models.Model):
    """Таблица с техническими параметрами дома.

            Сокращения:
        MOP - места общего пользования
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    MOP = models.DecimalField(verbose_name="Площадь мест общего пользования",
                              max_digits=5, decimal_places=2,
                              help_text="метры квадратные")
    norm_cold_water = models.DecimalField(verbose_name="Норматив горячего \
                                          водоснабжения",
                                          max_digits=3,
                                          decimal_places=2,
                                          help_text="тонн на метр квадратный")
    norm_hot_water = models.DecimalField(verbose_name="Норматив холодного \
                                         водоснабжения",
                                         max_digits=3,
                                         decimal_places=2,
                                         help_text="тонн на метр квадратный")
    norm_heating = models.DecimalField(verbose_name="Норматив отопления или \
                                       подогрев",
                                       max_digits=5,
                                       decimal_places=4,
                                       help_text="Гкал на метр квадратный")

    class Meta:
        ordering = ["home"]
        verbose_name = "Параметры дома"
        verbose_name_plural = "Параметры домов"
        unique_together = ('home', 'MOP')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.MOP), " кв.м."))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.MOP)))


class ConsumptionODPU(models.Model):
    """Таблица с текущими показаниями общедомового прибора учёта.

    """
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    temp1 = models.DecimalField(verbose_name="T1", max_digits=6,
                                decimal_places=2)
    temp2 = models.DecimalField(verbose_name="T2", max_digits=6,
                                decimal_places=2)
    G1 = models.DecimalField(verbose_name="G1", max_digits=5,
                             decimal_places=2, default=0)
    G2 = models.DecimalField(verbose_name="G2", max_digits=5,
                             decimal_places=2, default=0)
    work_time = models.IntegerField("Время нормальной работы")
    idle_time = models.IntegerField("Время простоя")
    Q1 = models.DecimalField(verbose_name="Q1",
                             max_digits=10,
                             decimal_places=3)
    M1 = models.DecimalField(verbose_name="M1",
                             max_digits=10,
                             decimal_places=3)
    M2 = models.DecimalField(verbose_name="M1",
                             max_digits=10,
                             decimal_places=3)

    class Meta:
        ordering = ["home", "time_record"]
        verbose_name = "Показания ОДПУ"
        verbose_name_plural = "Показания ОДПУ"
        unique_together = ('home', 'resource_type', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record)))


class ConsumptionIPU(models.Model):
    """Таблица с показаниями индивидуальных приборов учёта
    по каждому жилому и нежилому помещению.

    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    apartment = models.ForeignKey(HomeApartment,
                                  on_delete=models.CASCADE)
    IPU_mass = models.DecimalField(verbose_name="Расход по ИПУ",
                                   max_digits=7,
                                   decimal_places=3,
                                   help_text="тонны")
    IPU_calories = models.DecimalField(verbose_name="Расход по ИПУ",
                                       max_digits=8,
                                       decimal_places=6,
                                       help_text="Гкал")
    recalculation_mass = models.DecimalField(verbose_name="Перерасчёт",
                                             max_digits=7,
                                             decimal_places=3,
                                             help_text="тонны")
    recalculation_calories = models.DecimalField(verbose_name="Перерасчёт",
                                                 max_digits=8,
                                                 decimal_places=6,
                                                 help_text="Гкал")

    class Meta:
        ordering = ["home", "apartment"]
        verbose_name = "Показания ИПУ"
        verbose_name_plural = "Показания ИПУ"
        unique_together = ('home', 'apartment', 'time_record')

    def __str__(self):
        return "".join((str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))


class ConsumptionRSO(models.Model):
    """Таблица с расчётными параметрами общедомовых нужд,
    рассчитываемых ресурсоснабжающими организациями.

        Сокращения:
        ODPU - общедомовой прибор учёта
        IPU - индивидуальный прибор учёта
        RP - жилое помещение
        nonRP - нежилое помещение
        ODN - общедомовые нужды
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    ODPU_mass = models.DecimalField(verbose_name="Расход по ОДПУ",
                                    max_digits=8,
                                    decimal_places=3,
                                    help_text="тонн")
    ODPU_calories = models.DecimalField(verbose_name="Расход по ОДПУ",
                                        max_digits=9,
                                        decimal_places=5,
                                        help_text="Гкал")
    IPU_RP_mass = models.DecimalField(verbose_name="Расход по ИПУ (жилые пом.)",
                                      max_digits=8,
                                      decimal_places=3,
                                      help_text="тонн")
    IPU_RP_calories = models.DecimalField(verbose_name="Расход по ИПУ (жилые пом.)",
                                          max_digits=9,
                                          decimal_places=5,
                                          help_text="Гкал")
    IPU_nonRP_mass = models.DecimalField(verbose_name="Расхо по ИПУ (нежил. пом.)",
                                         max_digits=8,
                                         decimal_places=3,
                                         help_text="тонн")
    IPU_nonRP_calories = models.DecimalField(verbose_name="Расход по ИПУ (неж. пом)",
                                             max_digits=9,
                                             decimal_places=5,
                                             help_text="Гкал")
    ODN_mass = models.DecimalField(verbose_name="Расход по ОДН",
                                   max_digits=8,
                                   decimal_places=3,
                                   help_text="тонн")
    ODN_calories = models.DecimalField(verbose_name="Расход по ОДН",
                                       max_digits=9,
                                       decimal_places=5,
                                       help_text="Гкал")
    negative_ODN_mass = models.DecimalField(verbose_name="Отрицательный ОДН",
                                            max_digits=8,
                                            decimal_places=3,
                                            help_text="тонн")
    negative_ODN_calories = models.DecimalField(verbose_name="Отрицательный ОДН",
                                                max_digits=9,
                                                decimal_places=5,
                                                help_text="Гкал")
    result_ODN_mass = models.DecimalField(verbose_name="Итоговый ОДН",
                                          max_digits=8,
                                          decimal_places=3,
                                          help_text="тонн")
    result_ODN_calories = models.DecimalField(verbose_name="Итоговый ОДН",
                                              max_digits=9,
                                              decimal_places=5,
                                              help_text="Гкал")
    payable_ODN_mass = models.DecimalField(verbose_name="ОДН к начислению",
                                           max_digits=8,
                                           decimal_places=3,
                                           help_text="тонн")
    payable_ODN_calories = models.DecimalField(verbose_name="ОДН к начислению",
                                               max_digits=9,
                                               decimal_places=5,
                                               help_text="тонн")

    class Meta:
        ordering = ["home"]
        verbose_name = "Показания РСО"
        verbose_name_plural = "Показания РСО"
        unique_together = ('home', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, " : ",
                        str(self.home), ": ", str(self.time_record)))


class ResourceCharge(models.Model):
    """Таблица с рассчётом платы за общедомовые нужды.

    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    normative = models.DecimalField(verbose_name="Норматив",
                                    max_digits=6,
                                    decimal_places=3,
                                    help_text="тонн на метр квадратный")
    tarif = models.DecimalField(verbose_name="Тариф",
                                max_digits=5,
                                decimal_places=2,
                                help_text="рублей за тонну")
    nalog = models.IntegerField("Налог", default=0)

    class Meta:
        ordering = ["home", "time_record"]
        verbose_name = "Расчёт ресурсов"
        verbose_name_plural = "Расчёт ресурсов"
        unique_together = ('home', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), ": ", str(self.time_record)))
