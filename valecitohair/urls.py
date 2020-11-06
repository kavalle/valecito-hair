from django.contrib import admin
from django.urls import path, include
from valecitohair import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.home, name="index")
]
