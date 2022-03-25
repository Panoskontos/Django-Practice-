from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from dishes.models import *

# Imports for class based views
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Redirecting
from django.urls import reverse_lazy

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


# Creating CRUD with 3 lines
class SaladList(ListView):
    template_name = "salad_list.html"
    context_object_name = "salads"
    model = Salad


# Class Based Views for Person
# You won't focus on the code
# However you need them for job
# Don't use them to use them
# Use what is comfortable

class PersonList(ListView):
    # List
    model = Person
    context_object_name = 'people'
    paginate_by = 5
    # ordering = ['name']
    # you can search for other attributes to customize
    template_name = 'dishes/people.html'


class PersonDetail(DetailView):
    # Detail
    model = Person
    context_object_name = 'person'
    pk_url_kwargs = 'name'


class PersonCreate(CreateView):
    # Create
    model = Person
    fields = ['name', 'surname']
    success_url = reverse_lazy('people')


class PersonUpdate(UpdateView):
    # Update
    model = Person
    fields = ['name', 'surname']
    success_url = reverse_lazy('people')


class PersonDelete(DeleteView):
    # Update
    model = Person
    context_object_name = 'person'
    success_url = reverse_lazy('people')


# All class based views inherit from View, this is how you can customize
# class PersonView(View):
#     pass
