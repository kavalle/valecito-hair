from django.contrib import admin
from django.urls import path, include
from main.views import list

from django.contrib.auth.views import LoginView,logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('listar/', list, name="listar"),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/',logout_then_login,name="logout"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls'))
]

# path('listar/',LoginView.as_view(template_name='listar.html'),name="listar"),

