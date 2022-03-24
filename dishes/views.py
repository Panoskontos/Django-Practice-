from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from dishes.models import *
from django.views.generic import ListView
from .forms import *
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


def login(request):
    if request.method == 'POST':
        form = SaladForm(request.POST)
        if form.is_valid():
            print('form is valid')
            return HttpResponseRedirect('/dishes/thankyou')
    else:
        form = SaladForm()
    context = {
        'form': form,
    }
    return render(request, 'dishes/login.html', context)


def thankyou(request):
    return render(request, 'dishes/thankyou.html')


class SaladList(ListView):
    template_name = "salad_list.html"
    context_object_name = "salads"
    model = Salad

