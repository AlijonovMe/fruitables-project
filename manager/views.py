import random

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import *
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime
from django.views import View

from .models import *


class HomeListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = Product.objects.all()

        if len(products) >= 8:
            product_list = random.sample(list(products), 8)
        else:
            product_list = products

        return product_list


class ProductsByDepartment(HomeListView):
    template_name = 'shop.html'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        department = get_object_or_404(Departament, slug=self.kwargs.get('department_slug'))
        categories = Category.objects.filter(departament=department).select_related('departament')

        products = Product.objects.filter(category__departament=department).select_related('category')
        featured_products = Product.objects.filter(category__departament=department, discount__gt=0).select_related(
            'category')

        paginator = Paginator(products, self.paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.page(page_number)

        context.update({
            'department': department,
            'categories': categories,
            'page_obj': page_obj,
            'featured_products': featured_products[:3],
            'all_featured_products': featured_products[3:]
        })

        return context


class ProductsByCategory(ProductsByDepartment):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        department = get_object_or_404(Departament, slug=self.kwargs.get('department_slug'))
        category = get_object_or_404(Category, slug=self.kwargs.get('category_slug'))

        categories = Category.objects.filter(departament=department).select_related('departament')
        featured_products = Product.objects.filter(category=category, discount__gt=0).select_related('category')

        paginator = Paginator(
            Product.objects.filter(category=category).select_related('category'),
            self.paginate_by
        )

        page_obj = paginator.page(self.request.GET.get('page', 1))

        context.update({
            'department': department,
            'categories': categories,
            'page_obj': page_obj,
            'featured_products': featured_products[:3],
            'all_featured_products': featured_products[3:]
        })

        print(context)

        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop-detail.html'
    slug_url_kwarg = 'product_slug'

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get('product_slug'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        department = get_object_or_404(Departament, slug=self.kwargs.get('department_slug'))
        category = get_object_or_404(Category, slug=self.kwargs.get('category_slug'))

        categories = Category.objects.filter(departament=department).select_related('departament')
        products = Product.objects.filter(category=category).select_related('category')
        featured_products = Product.objects.filter(category=category, discount__gt=0).select_related('category')

        context.update({
            'department': department,
            'categories': categories,
            'products': products,
            'featured_products': featured_products[:3],
            'all_featured_products': featured_products[3:]
        })

        print(context)

        return context


class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')


class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')


class Testimonial(View):
    def get(self, request):
        return render(request, 'testimonial.html')


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')


class NotFound(View):
    def get(self, request):
        return render(request, '404.html')
