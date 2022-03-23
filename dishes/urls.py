from django.urls import include, path
from . import views

# dishes url
urlpatterns = [
    path('<str:pk>', views.singles, name='single'),
]
