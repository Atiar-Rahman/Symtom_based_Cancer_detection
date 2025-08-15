from django.urls import path
from tools.views import Home,Detection,Knowledge,Contact,Breast_blog,Lung_blog,Liver_blog

urlpatterns = [
    path('detection/',Detection,name='detection'),
    path('knowledge/',Knowledge,name='knowledge'),
    path('contact/',Contact,name='contact'),
    path('breast_blog/',Breast_blog,name = 'breast'),
    path('lung_blog/',Lung_blog,name = 'lung'),
    path('liver_blog/',Liver_blog,name = 'liver'),
]
