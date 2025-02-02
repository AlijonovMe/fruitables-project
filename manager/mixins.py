from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class LoginNoRequired(AccessMixin):
    """
    LoginNoRequired mixini, foydalanuvchi tizimga kirgan bo'lsa, uni
    belgilangan 'login_url' (default holatda 'index') sahifasiga yo'naltiradi.
    Agar foydalanuvchi tizimga kirgan bo'lmasa, normal so'rovni davom ettiradi.
    """

    login_url = 'index'

    def dispatch(self, request, *args, **kwargs):
        """
        Foydalanuvchi tizimga kirgan bo'lsa, uni login_url (default holatda 'index') sahifasiga yo'naltiradi.
        Aks holda, so'rovni davom ettirib, asosan requestni uzatadi.
        """
        if request.user.is_authenticated:
            return redirect(self.get_login_url())
        return super().dispatch(request, *args, **kwargs)


class StaffRequired(AccessMixin):
    """
    StaffRequired mixini faqat admin yoki staff foydalanuvchilar uchun ishlaydi.
    Agar foydalanuvchi staff bo'lmasa, uni login_url (default holatda 'not_found') sahifasiga yo'naltiradi.
    """

    login_url = 'not_found'

    def dispatch(self, request, *args, **kwargs):
        """
        Foydalanuvchi staff bo'lmasa, 'login_url' (default holatda 'not_found') sahifasiga yo'naltiradi.
        Agar foydalanuvchi staff bo'lsa, so'rovni davom ettiradi.
        """
        if not request.user.is_staff:
            return redirect(
                self.get_login_url())
        return super().dispatch(request, *args, **kwargs)
