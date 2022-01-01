from django.urls import path, include
from bloghome import views


urlpatterns = [
    path('', views.home),
]