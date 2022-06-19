from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='myhood-home'),
    path('about/', views.about, name='myhood-about'),
]

