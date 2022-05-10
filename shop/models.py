from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва')
    content = models.TextField(blank=True, verbose_name='Опис')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    in_stock = models.BooleanField(default=True, verbose_name='В наявності')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категорія')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Товар '
        verbose_name_plural = 'Товари'
        ordering = ['-created', 'name']


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категорія '
        verbose_name_plural = 'Категорії'
        ordering = [ 'name']




