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


class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class Shop(View):
    def get(self, request):
        return render(request, 'shop.html')


class ShopDetail(View):
    def get(self, request):
        return render(request, 'shop-detail.html')


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