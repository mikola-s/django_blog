from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.get_name, name='index'),
    path('taken/', views.taken, name='taken'),
]
