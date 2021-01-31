from django.urls import path
from visitnepal2020 import views

urlpatterns=[
    path('register',views.register),
    path(('login'),views.log.login)]