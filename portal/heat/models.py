from django.db import models


class Home(models.Model):
    """Таблица с адресом дома

    """
    city = models.CharField(max_length=250)
    adress = models.CharField(max_length=250)
    home_number = models.IntegerField(max_length=4)
    home_sub_number = models.CharField(max_length=2,
                                       null=True)

    class Meta:
        ordering = ["city", "adress", "home_number"]


class HomeApartment(models.Model):
    """Таблица со списком жилых и нежилых помещений в доме

    Args:
        models ([type]): [description]
    """
    APARTMENTS = [
        ("residential", "Жилое"),
        ("non-residential", "Нежилое")
    ]

    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    number = models.IntegerField(max_length=4)
    apartment_type = models.CharField(max_length=15,
                                      choices=APARTMENTS,
                                      default="residential")

    class Meta:
        ordering = ["number"]


class ConsumptionODPU(models.Model):
    """Таблица с показаниями общедомового прибора учёта

    """
    RESOURCE = [
        ("cold_water", "Холодная вода"),
        ("hot_water", "Горячая вода"),
        ("heating", "Отопление"),
        ("drainage", "Водоотведение"),
        ("electricity", "Электричество")
    ]

    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=15,
                                     choices=RESOURCE,
                                     default="heating")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    time_record = models.DateField()
    temp1 = models.DecimalField(max_digits=6,
                                decimal_places=2)
    temp2 = models.DecimalField(max_digits=6,
                                decimal_places=2)
    G1 = models.DecimalField(max_digits=5,
                             decimal_places=2, null=True)
    G2 = models.DecimalField(max_digits=5,
                             decimal_places=2, null=True)
    work_time = models.IntegerField(max_digits=7)
    idle_time = models.IntegerField(max_digits=7)
    Q1 = models.DecimalField(max_digits=10,
                             decimal_places=3)
    M1 = models.DecimalField(max_digits=10,
                             decimal_places=3)
    M2 = models.DecimalField(max_digits=10,
                             decimal_places=3)

    class Meta:
        ordering = ["time_record"]


class ConsumptionIPU(models.Model):
    """Таблица с показаниями индивидуальных приборов учёта

    """
    home = home = models.ForeignKey(Home, on_delete=models.CASCADE)
    apartment = models.ForeignKey(HomeApartment,
                                  on_delete=models.SET_DEFAULT)
    IPU_mass = models.DecimalField(max_digits=7,
                                   decimal_places=3,
                                   default=0)
    IPU_calories = models.DecimalField(max_digits=8,
                                       decimal_places=6,
                                       default=0)
    recalculation_mass = models.DecimalField(max_digits=7,
                                             decimal_places=3,
                                             default=0)
    recalculation_calories = models.DecimalField(max_digits=8,
                                                 decimal_places=6,
                                                 default=0)

    class Meta:
        ordering = ["apartment"]


class ConsumptionRSO(models.Model):
    """Таблица с расчётными параметрами общедомовых нужд,
    рассчитываемых ресурсоснабжающими организациями
        Сокращения:
        ODPU - общедомовой прибор учёта
        IPU - индивидуальный прибор учёта
        RP - жилое помещение
        nonRP - нежилое помещение
        ODN - общедомовые нужды
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    expense_ODPU_mass = models.DecimalField(max_digits=8,
                                            decimal_places=3)
    expense_ODPU_calories = models.DecimalField(max_digits=9,
                                                decimal_places=5)
    expense_IPU_RP_mass = models.DecimalField(max_digits=8,
                                              decimal_places=3)
    expense_IPU_RP_calories = models.DecimalField(max_digits=9,
                                                  decimal_places=5)
    expense_IPU_nonRP_mass = models.DecimalField(max_digits=8,
                                                 decimal_places=3)
    expense_IPU_nonRP_calories = models.DecimalField(max_digits=9,
                                                     decimal_places=5)
    expense_ODN_mass = models.DecimalField(max_digits=8,
                                           decimal_places=3)
    expense_ODN_calories = models.DecimalField(max_digits=9,
                                               decimal_places=5)
    negative_ODN_mass = models.DecimalField(max_digits=8,
                                            decimal_places=3)
    negative_ODN_calories = models.DecimalField(max_digits=9,
                                                decimal_places=5)
    result_ODN_mass = models.DecimalField(max_digits=8,
                                          decimal_places=3)
    result_ODN_calories = models.DecimalField(max_digits=9,
                                              decimal_places=5)
    payable_ODN_mass = models.DecimalField(max_digits=8,
                                           decimal_places=3)
    payable_ODN_calories = models.DecimalField(max_digits=9,
                                               decimal_places=5)

    class Meta:
        ordering = ["home"]


class ResourceCharge(models.Model):
    """Таблица с рассчётом платы за общедомовые нужды

    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    time_record = models.DateField()
    normative = models.DecimalField(max_digits=6,
                                    decimal_places=3)
    tarif = models.DecimalField(max_digits=5,
                                decimal_places=2)
    nalog = models.IntegerField(max_length=2)

    class Meta:
        ordering = ["time_record"]


class HomeParametrs(models.Model):
    """Таблица с параметрами дома
            Сокращения:
        MOP - места общего пользования
    """
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    MOP = models.DecimalField(max_digits=5,
                              decimal_places=2)
    normative_mass = models.DecimalField(max_digits=3,
                                         decimal_places=2)
    normative_calories = models.DecimalField(max_digits=5,
                                             decimal_places=4)

    class Meta:
        ordering = ["home"]
