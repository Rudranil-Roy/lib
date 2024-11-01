
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('addbook/', views.addbook,name='addbook'),
    path('addreader/', views.addreader,name='addreader'),
    path('reader/<str:pk>/', views.reader,name='reader'),
    path('login/', views.loginp,name='login'),
    path('logout/', views.logoutp,name='logout'),
    path('togglestatus/<str:pk>/', views.togglestatus,name='togglestatus'),
    path('deleteuser/<str:pk>/', views.deleteuser,name='deleteuser'),
    path('returnbook/<str:pk>/', views.returnbook,name='returnbook'),
    path('updatebook/<str:pk>/', views.updatebook,name='updatebook'),
    path('deletebook/<str:pk>/', views.deletebook,name='deletebook'),
]
