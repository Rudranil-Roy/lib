
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('addreader/', views.addreader,name='addreader'),
    path('reader/<str:pk>/', views.reader,name='reader'),
]
