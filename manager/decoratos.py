from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps


def staff_required(view_func=None, login_url=None):
    """
    staff_required dekoratori faqat staff foydalanuvchilari uchun mo'ljallangan.
    Agar foydalanuvchi staff bo'lmasa, `login_url` sahifasiga yoki
    `PermissionDenied` xatosiga yo'naltiriladi.

    :param view_func: Foydalaniladigan view funksiyasi (optional).
    :param login_url: Foydalanuvchi staff bo'lmasa, yo'naltiriladigan URL (optional).
    :return: View funksiyasiga o'zgartirish kiritadigan dekorator.
    """

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_staff:
                if login_url:
                    login_url_resolved = reverse(login_url)
                    return redirect(login_url_resolved)
                raise PermissionDenied
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if view_func:
        return decorator(view_func)
    return decorator


def login_not_required(name=None):
    """
    login_not_required dekoratori tizimga kirgan foydalanuvchiga ma'lum bir URL'ga
    yo'naltirilishiga imkon beradi. Agar foydalanuvchi tizimga kirgan bo'lsa,
    `name` URL'siga yoki `index` sahifasiga yo'naltiriladi.

    :param name: Agar foydalanuvchi tizimga kirgan bo'lsa, yo'naltiriladigan URL (optional).
    :return: View funksiyasiga o'zgartirish kiritadigan dekorator.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                if name:
                    return redirect(name)
                return redirect('index')
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
