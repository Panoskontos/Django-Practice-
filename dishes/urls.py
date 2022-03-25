from django.urls import include, path
from .views import *


# dishes url
urlpatterns = [
    # path('<str:pk>', views.singles, name='single'),
    path('login', login, name="login"),
    path('thankyou', thankyou, name="thankyou"),
    path('salad/', SaladList.as_view()),

    # Class based view url
    path('people/', PersonList.as_view(), name="people"),
    path('person/<str:pk>', PersonDetail.as_view(), name="person"),
    path('person-create/', PersonCreate.as_view(), name="person-create"),
    path('person-update/<str:pk>', PersonUpdate.as_view(), name="person-update"),
    path('person-delete/<str:pk>', PersonDelete.as_view(), name="people-delete"),

    # You need to also create templates
]
