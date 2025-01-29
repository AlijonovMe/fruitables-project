from django.shortcuts import get_list_or_404
from django import template

from ..models import *


register = template.Library()


@register.simple_tag
def all_departament():
    return get_list_or_404(Departament)


@register.simple_tag
def all_category():
    return get_list_or_404(Category)


@register.simple_tag
def cart_item_count(request):
    products: dict = request.session.get('products', {})
    return len(products)