from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #views.index - name of function in views.py
    #path('add_finops/', views.add_finops, name='add_finops'),
]