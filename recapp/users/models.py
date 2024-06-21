from django.contrib.auth.models import AbstractUser
from django.db import models


class CategoryRecept(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Recept(models.Model):
    recept_name = models.CharField(max_length=50, verbose_name="Название блюда")
    category = models.ManyToManyField(CategoryRecept, verbose_name="Категория")
    ingredients = models.TextField(verbose_name="Ингридиенты")
    description = models.TextField(verbose_name="Описание")
    cooking_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.CharField(max_length=10, verbose_name="Время приготовления")
    image = models.ImageField(upload_to='foto/%Y/%m/%d', default=None, verbose_name="Фото")
    author = models.TextField(max_length=30, verbose_name="Автор")
    date_of_addition = models.DateField(auto_now=True)

    def __str__(self):
        return self.recept_name, self.category


