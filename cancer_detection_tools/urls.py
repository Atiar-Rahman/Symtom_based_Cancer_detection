
from django.contrib import admin
from django.urls import path,include
from tools.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tools/',include('tools.urls')),
    path('', Home, name='home'),
]
