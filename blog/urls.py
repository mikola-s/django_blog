from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('selection_def/', views.selection_def_view, name='selection_def'),
    path('selection_class/', views.SelectionClassFormView.as_view(), name='selection_class'),
    path('accepted/', views.accepted, name='thanks'),
]
