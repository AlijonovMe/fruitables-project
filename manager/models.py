from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True, verbose_name='Telefon raqam')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Profil surati')

    class Meta:
        verbose_name = 'Foydalanuvchi '
        verbose_name_plural = 'Foydalanuvchilar'


class Departament(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nomi')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Identifikatori')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bo'lim "
        verbose_name_plural = "Bo'limlar"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nomi')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Identifikatori')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, related_name='departament',
                                    verbose_name="Bo'limi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya '
        verbose_name_plural = 'Kategoriyalar'


TYPES = {
    'kg': "kg",
    'g': "g",
    'mg': "mg",
    'l': "l",
    'ml': "ml"
}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nomi')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Identifikatori')
    description = models.TextField(null=True, blank=True, verbose_name='Tavsifi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Chegirma narxi', help_text='Chegirma narxini kiriting. Masalan: 10000')
    quantity = models.IntegerField(default=15, verbose_name='Miqdori')
    quality = models.CharField(max_length=10, verbose_name='Sifati')
    weight = models.CharField(max_length=2, choices=TYPES, verbose_name="O'lchov birligi")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Surati')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Mahsuloti')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Mahsulot surati '
        verbose_name_plural = 'Mahsulot suratlari'
