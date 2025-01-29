from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
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
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, related_name='category',
                                    verbose_name="Bo'limi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya '
        verbose_name_plural = 'Kategoriyalar'


WEIGHT_TYPES = {
    'kg': "Kilogram",
    'g': "Gram",
    'mg': "Milligram",
    'l': "Litr",
    'ml': "Milliliter"
}

CURRENCY_TYPES = {
    'UZS': "UZS",
}


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nomi')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Identifikatori')
    description = models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi')
    currency = models.CharField(max_length=3, choices=CURRENCY_TYPES, verbose_name='Valyuta')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi', validators=[MinValueValidator(0)])
    discount = models.IntegerField(default=0, verbose_name='Chegirma foizi',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   help_text='Agar mahsulotingizga chegirma qo‘ymoqchi bo‘lsangiz, chegirma foizini (masalan, 50) kiriting. Agar chegirma bermoqchi bo‘lmasangiz, bu maydonga tegmang.')
    quantity = models.IntegerField(default=0, verbose_name='Miqdori', validators=[MinValueValidator(0)],)
    quality = models.CharField(max_length=10, verbose_name='Sifati')
    weight = models.CharField(max_length=2, choices=WEIGHT_TYPES, verbose_name="O'lchov birligi")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)

    def __str__(self):
        return self.name

    def get_discount_price(self):
        if self.discount > 0:
            discount_price = self.price - (self.price * self.discount) / 100
            return discount_price
        return None

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name='Rasmi (500x350)',
                              help_text="Rasmning o‘lchami 500x350 piksel bo‘lishi kerak. Iltimos, to‘g‘ri o‘lchamdagi rasmni yuklang!")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Mahsuloti')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Mahsulot surati '
        verbose_name_plural = 'Mahsulot suratlari'
