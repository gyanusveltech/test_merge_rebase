
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', mainView.as_view(), name = "home"),
]
