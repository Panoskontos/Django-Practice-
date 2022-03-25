from django.urls import include, path
from .views import *

# # path('<str:pk>', views.singles, name='single'),
# dishes url
urlpatterns = [

    path('login', login, name="login"),
    path('thankyou', thankyou, name="thankyou"),
    path('salad/', SaladList.as_view()),
    path('import-file/', upload_files, name='import-file'),
    path('import-books/', upload_book, name='import-book'),

    # Class based view url
    path('people/', PersonList.as_view(), name="people"),
    path('person/<str:pk>', PersonDetail.as_view(), name="person"),
    path('person-create/', PersonCreate.as_view(), name="person-create"),
    path('person-update/<str:pk>', PersonUpdate.as_view(), name="person-update"),
    path('person-delete/<str:pk>', PersonDelete.as_view(), name="people-delete"),

    # You need to also create templates

    # success
    # fail
    path('success/<str:message>', success, name='success'),
    path('fail/<str:message>', fail, name='fail'),


    # CRUD Views
    # Read
    path('products', products, name="products"),
    path('products/<str:pk>', product, name="product"),
    path('create-product', create_product, name="create-product"),
]
