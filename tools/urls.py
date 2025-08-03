from django.urls import path
from tools.views import Home,Detection,Knowledge,Contact

urlpatterns = [
    path('detection/',Detection,name='detection'),
    path('knowledge/',Knowledge,name='knowledge'),
    path('contact/',Contact,name='contact'),
]
