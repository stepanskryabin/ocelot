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
