from django.urls import path
from tools.views import Home,Detection,Knowledge

urlpatterns = [
    path('detection/',Detection,name='detection'),
    path('knowledge/',Knowledge,name='knowledge')
]
