from django.urls import path
from . import views

urlpatterns = [
    # /register/
    path('', views.index, name='register')
    ]