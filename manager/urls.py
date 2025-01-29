from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),

    path('department/<slug:department_slug>/', ProductsByDepartment.as_view(), name='department'),
    path('department/<slug:department_slug>/<slug:category_slug>/', ProductsByCategory.as_view(), name='category'),
    path('department/<slug:department_slug>/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product'),
    path('cart/<slug:product_slug>/add', CartAction.as_view(), name='add-to-cart'),
    path('cart/<slug:product_slug>/update', CartAction.as_view(), name='update-to-cart'),
    path('cart/<slug:product_slug>/delete', DeleteCart.as_view(), name='delete-to-cart'),

    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', Checkout.as_view(), name='check-out'),
    path('testimonial/', Testimonial.as_view(), name='testimonial'),
    path('contact/', Contact.as_view(), name='contact'),
    path('not-found/', NotFound.as_view(), name='not-found'),
]