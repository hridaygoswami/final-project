from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='Index'),
    path("dashboard/", views.dashboard, name='Dashboard'),
    path("redirect/", views.redirect, name='Redirect')
]