from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('check/', views.check, name='check'),
	path('dangxuat/', views.dangxuat, name='dangxuat'),
	path('home/', views.home, name='home'),
	path('congno/phong=<int:stt>/', views.phong, name='phong'),
	path('congno/phong=<int:stt>/<str:thang>/<str:nam>/', views.congnothangchitiet , name='congnothangchitiet'),
	path('tinhtien/', views.tinhtien, name='tinhtien'),
]