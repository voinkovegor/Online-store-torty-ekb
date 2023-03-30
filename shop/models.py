from django.db import models
from django.urls import reverse, reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shop:product_list_by_category',
                            args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=1500)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    choice = models.BooleanField(default=False,
                                 verbose_name='Конструктор')

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Topping(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='topping/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Начинка'
        verbose_name_plural = 'Начинки'

    def __str__(self):
        return self.name


class Dekor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='topping/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Декор'
        verbose_name_plural = 'Декоры'

    def __str__(self):
        return self.name
