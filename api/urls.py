from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blocks/latest', views.block_latest, name='block_latest')
]