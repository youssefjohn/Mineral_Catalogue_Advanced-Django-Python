from . import views
from django.urls import path

app_name = "rocks"

urlpatterns = [

    path('home/<str:letter>/', views.index_view, name="index"),
    path('mineral/<int:pk>/', views.details_view, name="details"),
    path('home/random/random/', views.random_view, name="random"),


]
