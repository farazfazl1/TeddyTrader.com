from django.urls import path
from teddyBears import views

app_name = "teddyBears"

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.teddybear, name='teddy-bear'),
    path('search/', views.search, name='search'),
]
