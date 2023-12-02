#        .\api\urls.py

# ------------------------------ IMPORTS ------------------------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem)
]