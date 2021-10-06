from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', context={
        'page_name': 'Главная'
    })


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')
