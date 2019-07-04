from django.urls import path

from . import views

urlpatterns = [
    path('', views.CalcView.as_view(), name='calc'),
]
