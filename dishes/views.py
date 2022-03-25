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
    paginate_by = 10
    template_name = 'dishes/people.html'
    # you can search for other attributes to customize


class PersonDetail(DetailView):
    # Detail
    model = Person
    context_object_name = 'person'


class PersonCreate(CreateView):
    # Create
    model = Person
    success_url = reverse_lazy('people')
    form_class = PersonForm


class PersonUpdate(UpdateView):
    # Update
    model = Person
    fields = '__all__'
    # It is fields or form_class
    success_url = reverse_lazy('people')


class PersonDelete(DeleteView):
    # Delete
    model = Person
    context_object_name = 'person'
    success_url = reverse_lazy('people')


# All class based views inherit from View, this is how you can customize
# class PersonView(View):
#     pass


# Success and fail views
def success(request, message=None):
    return render(request, 'dishes/success.html', {'message': message})


def fail(request, message=None):
    return render(request, 'dishes/fail.html', {'message': message})

# use them with " return redirect('success', message='blah blah')


# Upload Files
def upload_files(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('success', message='File was successfully saved ')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'dishes/import_file.html', context)


# Uploading a book
def uniqueName(name):
    name = name + '-' + str(uuid.uuid1())
    return name


def upload_book(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = UploadBook(request.POST, request.FILES)
        if form.is_valid():

            formFile = request.FILES['book']

            # It is good practice to have uuid with files
            formFile.name = uniqueName(formFile.name)

            formTitle = request.POST.get('title')
            formAuthor = request.POST.get('author')
            # Save in books
            book = Book(title=formTitle, book=formFile, author=formAuthor)
            book.save()

            return redirect('thankyou')
    else:
        form = UploadBook()
    context = {
        'form': form,
        'books': books,
    }
    return render(request, 'dishes/books.html', context)


# Read
# List
def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'dishes/products.html', context)

# Single


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'dishes/product.html', context)


# Create
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        # print(request.POST)
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
            # or redirect success

    context = {
        'form': form,
    }
    return render(request, 'dishes/create-product.html', context)


# Update
# Almost same with Create
def update_product(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {
        'form': form,
    }
    return render(request, 'dishes/create-product.html', context)

# Delete


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('success', message='Item was deleted')
    context = {
        'product': product,
    }
    return render(request, 'dishes/delete-product.html', context)
