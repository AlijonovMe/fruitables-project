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


class Home(ListView):
    model = Product
    template_name = 'index.html'
