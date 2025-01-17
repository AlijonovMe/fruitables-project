from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('shop/', Shop.as_view(), name='shop'),
    path('shop-detail/', ShopDetail.as_view(), name='shop-detail'),
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', Checkout.as_view(), name='check-out'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('contact/', Contact.as_view(), name='contact'),
    path('not-found/', NotFound.as_view(), name='not-found'),
]