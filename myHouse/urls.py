from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('home/', views.home, name='home'),
	path('home/phong/<int:id>/', views.phong, name='phong'),
	path('home/phong/<int:id>/<str:thang>/<str:nam>', views.congnothang , name='congnothang'),

]