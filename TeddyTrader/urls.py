from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #---pages-----------------------------------------------
    path('', include('pages.urls'))
]
