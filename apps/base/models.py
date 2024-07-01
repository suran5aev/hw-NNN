from django.db import models

# Create your models here.
class Base(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='image/',
        verbose_name="Логотип сайта"
    )
    banner = models.ImageField(
        upload_to='banner/',
        verbose_name="Фото баннера"
    )
    phone = models.IntegerField(
        verbose_name="Номер телефона",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank=True, null=True        
    )
    instagram = models.URLField(
        verbose_name="instagram",
        blank=True, null=True        
    )
    location = models.CharField(
        max_length=255, 
        verbose_name="Адрес"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
        
class Popular_category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание блюда"
    )
    photo = models.ImageField(
        upload_to="popular_category/",
        verbose_name="Фото блюда"
    )
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Популярная категория"
        verbose_name_plural = "Популярные категории"

class Our_chef(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя Шеф-повара"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип повара"
    )
    photo = models.ImageField(
        upload_to='photo_chef/',
        verbose_name="фото повара"
    )
    facebook = models.URLField(
        verbose_name="Facebook - повара",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="youtube - повара",
        blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta: 
        verbose_name = "Повар"
        verbose_name_plural = "Повара"

class News(models.Model):
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.TextField(
        verbose_name='Описание'
    )
    date_to = models.CharField(
        max_length=155,
        verbose_name='Дата создание 1'
    )
    date_form = models.CharField(
        max_length=155,
        verbose_name='Дата создание 2'
    )
    food1 = models.CharField(
        max_length=155,
        verbose_name='Еда 1'
    )
    food2 = models.CharField(
        max_length=155,
        verbose_name='Еда 2'
    )

    
    def str(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "Новости"