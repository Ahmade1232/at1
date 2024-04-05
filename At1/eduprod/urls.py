from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.index, name='index'),
]
