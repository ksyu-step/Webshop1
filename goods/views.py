from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'goods/index.html', context={
        'page_name': 'Kaталог',
        'page_app': 'goods',
        'page_view': 'index',
        'all_products': Product.objects.all()
    })
