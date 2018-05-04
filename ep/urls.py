from django.urls import path

from . import views

app_name = 'ep'

urlpatterns = [
    path('', views.summary, name='summary'),
    path('new/', views.new, name='new'),
    path('create_entry/', views.create_entry, name='create_entry'),
]