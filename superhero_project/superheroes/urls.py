from django.urls import path
from django.urls import path

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name= 'detail'),
    path('new/', views.create, name='create'),
    path('new/', views.delete, name='delete'),
    path('<int:hero_id>/', views.edit, name='edit'),
]