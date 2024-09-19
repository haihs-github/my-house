from django.shortcuts import render, redirect
from .models import Phong, Congno
from datetime import datetime

# Create your views here.

def index(request):
	return redirect('/home')

def home(request):
	return render(request, 'home.html')

def getthangnam():
	thang = datetime.now().month
	year = datetime.now().year
	return str(thang) + "/" + str(year)

def getcongnobythangnam(congnos, date):
	newcongnos = []
	for x in congnos:
		if date in x.thang:
			newcongnos.append(x)
	return newcongnos

def getnam(thang):
	tmp = thang.split('/')
	return tmp[1]


def phong(request, id):
	phong = Phong.objects.get(id=id)
	congnos = Congno.objects.filter(phong=phong).order_by("-id")
	thangnam = getthangnam()
	thang = int(datetime.now().month)
	nam = int(datetime.now().year)
	nams = []
	tong = 0
	for x in congnos:
		if x.trangthai == False:
			tong = tong + x.tong
	for x in congnos:
		if getnam(x.thang) not in nams:
			nams.append(getnam(x.thang))
	nams.sort(reverse=True)
	if request.method == "POST":
		newnam = request.POST['nam']
		newcongnos = getcongnobythangnam(congnos, newnam)
		for x in newcongnos:
			if x.trangthai == False:
				tong = tong + x.tong
		context = {
			'phong': phong,
			'congnos': newcongnos,
			'thangnam': thangnam,
			'thang': thang,
			'nam': newnam,
			'nams': nams,
			'tong': tong,
		}
		print(context)
		return render(request, 'phong.html', context)
	context = {
		'phong': phong,
		'congnos': congnos,
		'thangnam': thangnam,
		'thang': thang,
		'nam': nam,
		'nams': nams,
		'tong': tong,
	}
	print(context)
	return render(request, 'phong.html', context)

def congnothang(request, id, thang, nam):
	phong = Phong.objects.get(id=id)
	thangnam = thang + "/" + nam
	congno = Congno.objects.get(phong=phong, thang=thangnam)
	tongsodien = phong.sodienthangnay - phong.sodienthangtruoc
	tongsonuoc = phong.sonuocthangnay - phong.sonuocthangtruoc
	context = {
		"phong": phong,
		"thangnam": thangnam,
		"congno": congno,
		"tongsodien": tongsodien,
		"tongsonuoc": tongsonuoc,
	}
	return render(request, 'congnothang.html', context)