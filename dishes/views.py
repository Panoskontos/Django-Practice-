from django.shortcuts import render
from dishes.models import *
# Create your views here.


def dashboard(request):
    # Logic
    burgers = Burger.objects.all()
    salads = Salad.objects.all()
    main_dishes = MainDish.objects.all()
    main_dishes_tag = MainDishTag.objects.all()

    # Data you want to connect
    context = {
        'burgers': burgers,
        'salads': salads,
        'main_dishes': main_dishes,
        'main_dishes_tag': main_dishes_tag,

    }
    # connect with url
    return render(request, 'dishes/dashboard.html', context)


def singles(request, pk):
    # Logic
    burger = Burger.objects.all().filter(name=pk)
    salad = Salad.objects.all().filter(name=pk)
    if burger:
        print('burger')
    # Data you want to connect
    context = {
        'burger': burger,
        'salad': salad,

    }
    # connect with url
    return render(request, 'dishes/single-dish.html', context)
