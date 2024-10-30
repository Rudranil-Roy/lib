
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('addreader/', views.addreader,name='addreader'),
    path('reader/<str:pk>/', views.reader,name='reader'),
    path('deleteuser/<str:pk>/', views.deleteuser,name='deleteuser'),
    path('returnbook/<str:pk>/', views.returnbook,name='returnbook'),
]
