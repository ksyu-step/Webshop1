from django.shortcuts import render
from django.http import JsonResponse
from .models import Order


def ajax_cart(request):
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')

    Order.objects.create(
        title=f'Order-{pid}/{uid}',
        product_id=pid,
        user_id=uid,
        status='Ожидание подтверждения'
    )

    user_orders = Order.objects.filter(user_id=uid)
    cost = 0
    for order in user_orders:
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)


def ajax_cart_display(request):
    response = dict()
    uid = request.GET.get('uid')
    user_orders = Order.objects.filter(user_id=uid)

    cost = 0
    for order in user_orders:
        cost += order.product.price

    response['cost'] = cost
    response['count'] = len(user_orders)
    return JsonResponse(response)


def index(request):
    orders = Order.objects.all()
    return render(request, 'orders/index.html', context={
        'page_name': 'Корзина',
        'page_app': 'orders',
        'page_view': 'index',
        'orders': orders
    })
