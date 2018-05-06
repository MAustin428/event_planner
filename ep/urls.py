from django.urls import path

from . import views

app_name = 'ep'

urlpatterns = [
    path('summary', views.summary, name='summary'),
    path('new/', views.new, name='new'),
    path('event/<pk>/', views.view_event, name='view_event'),
    path('edit/<pk>/', views.update, name='update'),
    path('history/<title>/', views.history, name='history'),
    path('send_history', views.send_history, name='send_history')
]
