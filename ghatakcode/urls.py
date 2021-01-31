from django.urls import path

from ghatakcode import views

urlpatterns = [
    path('',views.demo.index),
]