from django.db import models

from pasport import models as PasportModels

from .controller import READING_DATE
from .controller import current_date


class AbstractMain(models.Model):
    """Абстрактный класс с полями таблиц: адрес дома, дата создания,
    дата обновления.

    """
    home = models.ForeignKey(PasportModels.Home,
                             on_delete=models.CASCADE,
                             verbose_name="Адрес")
    created = models.DateField("Создано",
                               auto_now_add=True)
    updated = models.DateField("Обновлено",
                               auto_now=True)

    class Meta:
        abstract = True


class AbstractResource(models.Model):
    """Абстрактный класс с полями таблиц: тип ресурса.

    """
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")]

    resource_type = models.CharField("Тип коммунального ресурса",
                                     max_length=15,
                                     choices=RESOURCE,
                                     default="heating")

    class Meta:
        abstract = True


class AbstractTimeRecord(models.Model):
    """Абстрактный класс с полями таблиц: месяц фиксации показаний.

    """
    time_record = models.DateField("Дата снятия показаний",
                                   default=current_date,
                                   help_text=f"Если оставить пустым, \
                                   автоматически установится {READING_DATE}\
                                   -ое число текущего месяца \n")

    class Meta:
        abstract = True


class Odpu(AbstractMain,
           AbstractResource,
           AbstractTimeRecord,
           models.Model):
    """Таблица с текущими показаниями общедомового прибора учёта.

    """
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
    temp3 = models.DecimalField("T3, градусы Цельсия",
                                max_digits=6,
                                decimal_places=2,
                                default=0,
                                help_text="Если не заполнено \
                                значение поля = 0")
    g1 = models.DecimalField("G1, тонны в час",
                             max_digits=5,
                             decimal_places=2,
                             default=0,
                             help_text="Если не заполнено \
                             значение поля = 0")
    g2 = models.DecimalField("G2, тонны в час",
                             max_digits=5,
                             decimal_places=2,
                             default=0,
                             help_text="Если не заполнено \
                             значение поля = 0")
    work_time = models.IntegerField("Tуч, время учёта",
                                    default=0,
                                    help_text="Время работы счёта")
    idle_time = models.IntegerField("Tнар, время наработки",
                                    default=0,
                                    help_text="Время работы прибора")
    q1 = models.DecimalField("Q1, Гкал",
                             max_digits=10,
                             decimal_places=3,
                             default=0.0)
    q2 = models.DecimalField("Q2, Гкал",
                             max_digits=10,
                             decimal_places=3,
                             default=0.0)
    m1 = models.DecimalField("M1 (прямая), тонны",
                             max_digits=10,
                             decimal_places=3,
                             default=0.0)
    m2 = models.DecimalField("M2 (обратная), тонны",
                             max_digits=10,
                             decimal_places=3,
                             default=0.0)
    m3 = models.DecimalField("M2 (обратная), тонны",
                             max_digits=10,
                             decimal_places=3,
                             default=0.0)
    m = models.DecimalField("М (потребление), тонны",
                            max_digits=10,
                            decimal_places=3,
                            default=0.0)

    class Meta:
        ordering = ["home", "time_record", "resource_type"]
        verbose_name = "Показания ОДПУ"
        verbose_name_plural = "Показания ОДПУ"
        unique_together = ('home', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record)))


class ApartmentIpu(AbstractMain,
                   AbstractResource,
                   AbstractTimeRecord,
                   models.Model):
    """Таблица с показаниями индивидуальных приборов учёта
    по каждому жилому и нежилому помещению.

    """
    apartment = models.ForeignKey(PasportModels.HomeApartment,
                                  on_delete=models.CASCADE,
                                  verbose_name="Помещение")
    indication = models.DecimalField("Показание ИПУ, тонны",
                                     max_digits=7,
                                     decimal_places=2,
                                     default=0.0,
                                     help_text="тонны")
    consumption = models.DecimalField("Расход по ИПУ, тонны",
                                      max_digits=7,
                                      decimal_places=2,
                                      default=0.0,
                                      help_text="тонны")
    recalc_mass = models.DecimalField("Перерасчёт, тонны",
                                      max_digits=7,
                                      decimal_places=3,
                                      default=0.0,
                                      help_text="тонны")
    recalc_calories = models.DecimalField("Перерасчёт, Гкал",
                                          max_digits=7,
                                          decimal_places=3,
                                          default=0.0,
                                          help_text="Гкал")
    calories = models.DecimalField("Расход по ИПУ, Гкал",
                                   max_digits=7,
                                   decimal_places=4,
                                   default=0.0,
                                   help_text="Гкал")

    class Meta:
        ordering = ["home", "apartment"]
        verbose_name = "Показания ИПУ"
        verbose_name_plural = "Показания ИПУ"
        unique_together = ('home', 'apartment', 'time_record', 'resource_type')

    def __str__(self):
        return "".join((str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))

    def __repr__(self):
        return "".join((self.__class__.__name__, ": ",
                        str(self.home), " - ", str(self.time_record),
                        " - ", str(self.apartment)))


class HomeIpu(AbstractMain,
              AbstractResource,
              AbstractTimeRecord,
              models.Model):
    """Таблица с показаниями индивидуальных приборов учёта
    суммарно по дому.

    """
    mass = models.DecimalField("Расход по ИПУ, тонны",
                               max_digits=7,
                               decimal_places=2,
                               default=0.0,
                               help_text="тонны")
    calories = models.DecimalField("Расход по ИПУ, Гкал",
                                   max_digits=8,
                                   decimal_places=6,
                                   default=0.0,
                                   help_text="Если оставить пустым, \
                                   поле автоматически заполнится")

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


class Rso(AbstractMain,
          AbstractResource,
          AbstractTimeRecord,
          models.Model):
    """Таблица с расчётными параметрами общедомовых нужд,
    рассчитываемых ресурсоснабжающими организациями.

        Сокращения:
        ODPU - общедомовой прибор учёта
        IPU - индивидуальный прибор учёта
        RP - жилое помещение
        nonRP - нежилое помещение
        ODN - общедомовые нужды
    """
    ODPU_mass = models.DecimalField("Расход по ОДПУ, тонны",
                                    max_digits=8,
                                    decimal_places=3,
                                    default=0.0,
                                    help_text="тонн")
    ODPU_calories = models.DecimalField("Расход по ОДПУ, Гкал",
                                        max_digits=9,
                                        decimal_places=5,
                                        default=0.0,
                                        help_text="Гкал")
    IPU_RP_mass = models.DecimalField("Расход по ИПУ (жилые пом.), тонны",
                                      max_digits=8,
                                      decimal_places=3,
                                      default=0.0,
                                      help_text="тонн")
    IPU_RP_calories = models.DecimalField("Расход по ИПУ (жилые пом.), Гкал",
                                          max_digits=9,
                                          decimal_places=5,
                                          default=0.0,
                                          help_text="Гкал")
    IPU_nonRP_mass = models.DecimalField("Расхо по ИПУ (нежил. пом.), тонны",
                                         max_digits=8,
                                         decimal_places=3,
                                         default=0.0,
                                         help_text="тонн")
    IPU_nonRP_calories = models.DecimalField("Расход по ИПУ (неж. пом), Гкал",
                                             max_digits=9,
                                             decimal_places=5,
                                             default=0.0,
                                             help_text="Гкал")
    ODN_mass = models.DecimalField("Расход по ОДН, тонны",
                                   max_digits=8,
                                   decimal_places=3,
                                   default=0.0,
                                   help_text="тонн")
    ODN_calories = models.DecimalField("Расход по ОДН, Гкал",
                                       max_digits=9,
                                       decimal_places=5,
                                       default=0.0,
                                       help_text="Гкал")
    negative_ODN_mass = models.DecimalField("Отрицательный ОДН, тонны",
                                            max_digits=8,
                                            decimal_places=3,
                                            default=0.0,
                                            help_text="тонн")
    negative_ODN_calories = models.DecimalField("Отрицательный ОДН, Гкал",
                                                max_digits=9,
                                                decimal_places=5,
                                                default=0.0,
                                                help_text="Гкал")
    result_ODN_mass = models.DecimalField("Итоговый ОДН, тонны",
                                          max_digits=8,
                                          decimal_places=3,
                                          default=0.0,
                                          help_text="тонн")
    result_ODN_calories = models.DecimalField("Итоговый ОДН, Гкал",
                                              max_digits=9,
                                              decimal_places=5,
                                              default=0.0,
                                              help_text="Гкал")
    payable_ODN_mass = models.DecimalField("ОДН к начислению, тонный",
                                           max_digits=8,
                                           decimal_places=3,
                                           default=0.0,
                                           help_text="тонн")
    payable_ODN_calories = models.DecimalField("ОДН к начислению, Гкал",
                                               max_digits=9,
                                               decimal_places=5,
                                               default=0.0,
                                               help_text="тонн")

    class Meta:
        ordering = ["home", 'time_record']
        verbose_name = "Показания РСО"
        verbose_name_plural = "Показания РСО"
        unique_together = ('home', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, " : ",
                        str(self.home), ": ", str(self.time_record)))


class ResourceOdn(AbstractMain,
                  AbstractResource,
                  AbstractTimeRecord,
                  models.Model):
    """Таблица с расчётом объёма общедомовых нужд предъявляемых населению.
    """
    odn_mass = models.DecimalField("ОДН (масса)",
                                   max_digits=7,
                                   decimal_places=3,
                                   default=0.0,
                                   help_text="тонны")
    odn_gkal = models.DecimalField("ОДН (Гкал)",
                                   max_digits=7,
                                   decimal_places=3,
                                   default=0.0,
                                   help_text="Гкал")

    class Meta:
        ordering = ["home", "time_record"]
        verbose_name = "Расчёт ОДН"
        verbose_name_plural = "Расчёт ОДН"
        unique_together = ('home', 'time_record')

    def __str__(self):
        return "".join((str(self.home), ": ", str(self.time_record)))

    def __repr__(self):
        return "".join((self.__class__.__name__, " : ",
                        str(self.home), ": ", str(self.time_record)))


class ResourceChargeOdn(AbstractMain,
                        AbstractResource,
                        AbstractTimeRecord,
                        models.Model):
    """Таблица с расчётом платы за коммунальный ресурс
    на общедомовые нужды.

    """
    mass = models.DecimalField("Начислено населению, тонны",
                               max_digits=6,
                               decimal_places=3,
                               default=0.0,
                               help_text="")
    finance = models.DecimalField("Начисленно населению, руб.",
                                  max_digits=7,
                                  decimal_places=2,
                                  default=0.0,
                                  help_text="рублей")
    payed = models.DecimalField("Оплачено населением, руб.",
                                max_digits=6,
                                decimal_places=3,
                                default=0.0,
                                help_text="рублей")
    norm_mass = models.DecimalField("Объём по нормативу, тонны",
                                    max_digits=6,
                                    decimal_places=3,
                                    default=0.0,
                                    help_text="тонн на кв.м.")
    norm_finance = models.DecimalField("Объём по нормативу, руб.",
                                       max_digits=7,
                                       decimal_places=2,
                                       default=0.0,
                                       help_text="рублей")
    over_mass = models.DecimalField("Перерасход, тонны",
                                    max_digits=6,
                                    decimal_places=3,
                                    default=0.0,
                                    help_text="тонны")
    over_finance = models.DecimalField("Перерасход, рублей",
                                       max_digits=7,
                                       decimal_places=2,
                                       default=0.0,
                                       help_text="рублей")
    saldo_mass = models.DecimalField("Сальдо, тонны",
                                     max_digits=6,
                                     decimal_places=3,
                                     default=0.0,
                                     help_text="тонны")
    saldo_finance = models.DecimalField("Сальдо, руб.",
                                        max_digits=7,
                                        decimal_places=2,
                                        default=0.0,
                                        help_text="рублей")

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
