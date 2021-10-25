from django.urls import path
from .views import ajax_cart, ajax_cart_display, index


urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
    path('', index)
]
