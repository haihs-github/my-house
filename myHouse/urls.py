from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('home/congno/phong/<int:id>/', views.phong, name='phong'),
	path('home/congno/phong/<int:id>/check/<int:id2>', views.phongcheck, name='phongcheck'),
	path('home/congno/phong/<int:id>/<str:thang>/<str:nam>', views.congnothangchitiet , name='congnothangchitiet'),
	path('tinhtien/', views.tinhtien, name='tinhtien'),
]