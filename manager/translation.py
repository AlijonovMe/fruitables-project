from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Departament)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')