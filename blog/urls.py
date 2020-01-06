from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.MyFormView.as_view()),
    path('taken/', views.taken, name='taken'),
]
