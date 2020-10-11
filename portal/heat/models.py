from decimal import getcontext, Decimal
from datetime import date, datetime

from django.db import models

from pasport import models as pasport_models

# Дата снятия показаний ОДПУ и ИПУ, type int
READING_DATE = 18


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

    home = models.ForeignKey(pasport_models.Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата снятия показаний",
                                   blank=True,
                                   null=True,
                                   help_text=f"Если оставить пустым, \
                                   автоматически установится {READING_DATE} \
                                   число текущего месяца \n")
    temp1 = models.DecimalField("T1, градусы Цельсия",
                                max_digits=6,
                                decimal_places=2,
                                default=0,
                                help_text="Если не заполнено \
                                значение поля = 0")
    temp2 = models.DecimalField("T2, градусы Цельсия",
                                max_digits=6,
                                decimal_places=2,
                                default=0,
                                help_text="Если не заполнено \
                                значение поля = 0")
    G1 = models.DecimalField("G1, тонны в час",
                             max_digits=5,
                             decimal_places=2,
                             default=0,
                             help_text="Если не заполнено \
                             значение поля = 0")
    G2 = models.DecimalField("G2, тонны в час",
                             max_digits=5,
                             decimal_places=2,
                             default=0,
                             help_text="Если не заполнено \
                             значение поля = 0")
    work_time = models.IntegerField("Tуч, время учёта",
                                    help_text="Время работы счёта")
    idle_time = models.IntegerField("Tнар, время наработки",
                                    help_text="Время работы прибора")
    Q1 = models.DecimalField("Q1, Гкал",
                             max_digits=10,
                             decimal_places=3)
    M1 = models.DecimalField("M1, тонны",
                             max_digits=10,
                             decimal_places=3)
    M2 = models.DecimalField("M1, тонны",
                             max_digits=10,
                             decimal_places=3)

    def save(self, *args, **kwargs):
        if self.time_record is None:
            current = datetime.now()
            self.time_record = date(current.year, current.month, READING_DATE)
        super().save(*args, **kwargs)

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


class ConsumptionApartmentIPU(models.Model):
    """Таблица с показаниями индивидуальных приборов учёта
    по каждому жилому и нежилому помещению.

    """
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(pasport_models.Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата снятия показаний",
                                   blank=True,
                                   null=True,
                                   help_text=f"Если оставить пустым, \
                                   автоматически установится {READING_DATE} \
                                   число текущего месяца \n")
    apartment = models.ForeignKey(pasport_models.HomeApartment,
                                  on_delete=models.CASCADE,
                                  verbose_name="Помещение")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    IPU_indication = models.DecimalField("Показание ИПУ, тонны",
                                         max_digits=7,
                                         decimal_places=2,
                                         default=0,
                                         help_text="тонны")
    IPU_consumption = models.DecimalField("Расход по ИПУ, тонны",
                                          max_digits=7,
                                          decimal_places=2,
                                          default=0,
                                          help_text="тонны")
    IPU_calories = models.DecimalField("Расход по ИПУ, Гкал",
                                       max_digits=7,
                                       decimal_places=4,
                                       help_text="Гкал",
                                       default=0)
    recalculation_mass = models.DecimalField("Перерасчёт, тонны",
                                             max_digits=7,
                                             decimal_places=3,
                                             help_text="тонны",
                                             default=0)
    recalculation_calories = models.DecimalField("Перерасчёт, Гкал",
                                                 max_digits=7,
                                                 decimal_places=3,
                                                 help_text="Гкал",
                                                 default=0)

    def save(self, *args, **kwargs):
        if self.time_record is None:
            current = datetime.now()
            self.time_record = date(current.year, current.month, READING_DATE)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["home", "apartment"]
        verbose_name = "Показания ИПУ в помещениях"
        verbose_name_plural = "Показания ИПУ в помещениях"
        unique_together = ('home', 'apartment', 'time_record', 'resource_type')

    def __str__(self):
        return "".join((str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))


class ConsumptionHomeIPU(models.Model):
    """Таблица с показаниями индивидуальных приборов учёта
    суммарно по дому.

    """

    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(pasport_models.Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата снятия показаний",
                                   blank=True,
                                   null=True,
                                   help_text=f"Если оставить пустым, \
                                   автоматически установится {READING_DATE} \
                                   число текущего месяца \n")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    IPU_mass = models.DecimalField("Расход по ИПУ, тонны",
                                   max_digits=7,
                                   decimal_places=2,
                                   help_text="тонны",
                                   default=0)
    IPU_calories = models.DecimalField("Расход по ИПУ, Гкал",
                                       max_digits=8,
                                       decimal_places=6,
                                       help_text="Если оставить пустым, \
                                       поле автоматически заполнится",
                                       default=0)

    def save(self, *args, **kwargs):
        getcontext().prec = 5
        CONST = Decimal('0.0718')
        result = Decimal(self.IPU_mass) * CONST
        self.IPU_calories = float(result)
        if self.time_record is None:
            current = datetime.now()
            self.time_record = date(current.year, current.month, READING_DATE)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["home", "resource_type"]
        verbose_name = "Суммарные показания ИПУ"
        verbose_name_plural = "Суммарные показания ИПУ"
        unique_together = ('home', 'time_record', 'resource_type')

    def __str__(self):
        return "".join((str(self.home), " - ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record)))


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
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(pasport_models.Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    ODPU_mass = models.DecimalField("Расход по ОДПУ, тонны",
                                    max_digits=8,
                                    decimal_places=3,
                                    help_text="тонн")
    ODPU_calories = models.DecimalField("Расход по ОДПУ, Гкал",
                                        max_digits=9,
                                        decimal_places=5,
                                        help_text="Гкал")
    IPU_RP_mass = models.DecimalField("Расход по ИПУ (жилые пом.), тонны",
                                      max_digits=8,
                                      decimal_places=3,
                                      help_text="тонн")
    IPU_RP_calories = models.DecimalField("Расход по ИПУ (жилые пом.), Гкал",
                                          max_digits=9,
                                          decimal_places=5,
                                          help_text="Гкал")
    IPU_nonRP_mass = models.DecimalField("Расхо по ИПУ (нежил. пом.), тонны",
                                         max_digits=8,
                                         decimal_places=3,
                                         help_text="тонн")
    IPU_nonRP_calories = models.DecimalField("Расход по ИПУ (неж. пом), Гкал",
                                             max_digits=9,
                                             decimal_places=5,
                                             help_text="Гкал")
    ODN_mass = models.DecimalField("Расход по ОДН, тонны",
                                   max_digits=8,
                                   decimal_places=3,
                                   help_text="тонн")
    ODN_calories = models.DecimalField("Расход по ОДН, Гкал",
                                       max_digits=9,
                                       decimal_places=5,
                                       help_text="Гкал")
    negative_ODN_mass = models.DecimalField("Отрицательный ОДН, тонны",
                                            max_digits=8,
                                            decimal_places=3,
                                            help_text="тонн")
    negative_ODN_calories = models.DecimalField("Отрицательный ОДН, Гкал",
                                                max_digits=9,
                                                decimal_places=5,
                                                help_text="Гкал")
    result_ODN_mass = models.DecimalField("Итоговый ОДН, тонны",
                                          max_digits=8,
                                          decimal_places=3,
                                          help_text="тонн")
    result_ODN_calories = models.DecimalField("Итоговый ОДН, Гкал",
                                              max_digits=9,
                                              decimal_places=5,
                                              help_text="Гкал")
    payable_ODN_mass = models.DecimalField("ОДН к начислению, тонный",
                                           max_digits=8,
                                           decimal_places=3,
                                           help_text="тонн")
    payable_ODN_calories = models.DecimalField("ОДН к начислению, Гкал",
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
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(pasport_models.Home, on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано", auto_now_add=True)
    updated = models.DateField("Обновлено", auto_now=True)
    time_record = models.DateField("Дата")
    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    norm_mass = models.DecimalField("Норматив, тонны",
                                    max_digits=6,
                                    decimal_places=3,
                                    help_text="тонн на кв.м.")
    norm_finance = models.DecimalField("Норматив, руб.",
                                       max_digits=7,
                                       decimal_places=2,
                                       blank=True,
                                       null=True,
                                       help_text="рублей")
    over_in_weight = models.DecimalField("Перерасход, тонны",
                                         max_digits=6,
                                         decimal_places=3,
                                         blank=True,
                                         null=True,
                                         help_text="тонны")
    over_in_finance = models.DecimalField("Перерасход, рублей",
                                          max_digits=7,
                                          decimal_places=2,
                                          blank=True,
                                          null=True,
                                          help_text="рублей")
    accrued_mass = models.DecimalField("Начислено населению, тонны",
                                       max_digits=6,
                                       decimal_places=3,
                                       blank=True,
                                       null=True,
                                       help_text="тонны")
    accured_finance = models.DecimalField("Начисленно населению, руб.",
                                          max_digits=7,
                                          decimal_places=2,
                                          blank=True,
                                          null=True,
                                          help_text="рублей")
    saldo_mass = models.DecimalField("Сальдо, тонны",
                                     max_digits=6,
                                     decimal_places=3,
                                     blank=True,
                                     null=True,
                                     help_text="тонны")
    saldo_finance = models.DecimalField("Сальдо, руб.",
                                        max_digits=7,
                                        decimal_places=2,
                                        blank=True,
                                        null=True,
                                        help_text="рублей")
    payed = models.DecimalField("Оплачено населением, руб.",
                                max_digits=6,
                                decimal_places=3,
                                blank=True,
                                null=True,
                                help_text="рублей")
    tarif = models.DecimalField("Тариф",
                                max_digits=5,
                                decimal_places=2,
                                help_text="рублей за тонну")
    nalog = models.DecimalField("Налог",
                                max_digits=3,
                                decimal_places=1,
                                default=0)

    def save(self, *args, **kwargs):
        NORM = self.norm_mass
        TARIF = self.tarif
        NALOG = self.nalog
        self.norm_finance = (TARIF * (NORM + (NORM * (NALOG / Decimal('100')))))
        super().save(*args, **kwargs)

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
