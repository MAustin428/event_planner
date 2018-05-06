from django.urls import path

from . import views

app_name = 'ep'

urlpatterns = [
    path('summary', views.summary, name='summary'),
    path('new/', views.new, name='new'),
    path('event/', views.view_event, name='view_event'),
    path('edit/<pk>/', views.update, name='update'),
    
]
