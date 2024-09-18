from django.shortcuts import render, redirect
from .models import Phong, Congno

# Create your views here.

def index(request):
	return redirect('/home')

def home(request):
	return render(request, 'home.html')

def phong(request, id):
	phong = Phong.objects.get(id=id)
	congnos = Congno.objects.filter(phong=phong).order_by('-thang')
	context = {
		'phong': phong,
		'congnos': congnos,
	}
	return render(request, 'phong.html', context)