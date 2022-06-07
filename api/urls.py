from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view()), # login API URL Pattern
    path('books', views.BookView.as_view()) # login API URL Pattern
]

