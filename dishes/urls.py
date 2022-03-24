from django.urls import include, path
from .views import *


# dishes url
urlpatterns = [
    # path('<str:pk>', views.singles, name='single'),
    path('login', login, name="login"),
    path('thankyou', thankyou, name="thankyou"),
    path('salad/', SaladList.as_view()),

]
