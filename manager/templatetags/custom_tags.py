from django import template

from ..models import *


register = template.Library()


@register.simple_tag
def all_departament():
    return Departament.objects.all()


@register.simple_tag
def all_category():
    return Category.objects.all()


@register.simple_tag
def cart_item_count(request):
    products: dict = request.session.get('products', {})
    return len(products)