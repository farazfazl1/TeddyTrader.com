from django.urls import path
from teddyBears import views

app_name = "teddyBears"

urlpatterns = [
    path('', views.home, name='home'),
]
