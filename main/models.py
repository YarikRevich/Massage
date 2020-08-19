from django.db import models
from django.contrib.auth.models import User
import phone_field
from django.shortcuts import reverse, redirect


class ModificatedUser(models.Model):
    """
    In this model you can extand a native User model
    adding user's phone and his identificatior

    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    number = phone_field.PhoneField(
        blank=True, verbose_name="Номер телефона", unique=True)
    number_of_user = models.IntegerField(
        verbose_name="Номер пользователя", default=0)
    made_records = models.BooleanField(
        verbose_name="Делал ли записи", default=False)

    def __str__(self):
        return "{}".format(str(self.number_of_user))

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "moduser"
        verbose_name = "Дополнительная информация"
        verbose_name_plural = "Дополнительная информация"


class Service(models.Model):
    """In this model you can add a service"""

    name = models.CharField(
        max_length=200, verbose_name="Название услуги")
    description = models.CharField(
        max_length=400, verbose_name="Описание", default="-")
    price = models.IntegerField(
        verbose_name="Стоимость услуги")
    currency = models.CharField(
        max_length=10, verbose_name="Валюта")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse("ServiceInfo", kwargs={"pk": self.pk})

    class Meta:

        db_table = "services"
        verbose_name_plural = "Услуги"
        verbose_name = "Услуга"


class Record(models.Model):
    """This model is for adding user's record to the db"""

    author = models.ForeignKey(
        User, to_field="username", on_delete=models.CASCADE)
    name = models.CharField(
        max_length=30, verbose_name="Название услуги")
    description = models.CharField(
        max_length=200, verbose_name="Дополнительная информация")
    phone = models.ForeignKey(
        ModificatedUser, to_field="number", on_delete=models.CASCADE)
    time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время оформление записи")
    status = models.BooleanField(
        verbose_name="Статус", default=False)
    seen = models.BooleanField(
        verbose_name="Просмотрено врачём", default=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


    class Meta:

        db_table = "records"
        verbose_name_plural = "Записи"
        verbose_name = "Запись"


class Review(models.Model):
    """This model was made to save user's review"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=400, verbose_name="Отзыв")
    mark = models.IntegerField(
        verbose_name="Оценка")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.mark)}"

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse("Reviews", kwargs={"page": 1})
    

    class Meta:

        db_table = "reviews"
        verbose_name_plural = "Отзывы"
        verbose_name = "Отзыв"
        ordering = ("-time",)
