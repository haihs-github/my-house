from django.shortcuts import render, redirect
from .models import Phong, Congno
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return redirect('/home')

def home(request):
	phong1 = Phong.objects.get(id=1)
	congnosphong1 = Congno.objects.filter(phong=phong1)
	no1=0
	for x in congnosphong1:
		if x.trangthai == False:
			no1 += x.tong
	phong2 = Phong.objects.get(id=2)
	congnosphong2 = Congno.objects.filter(phong=phong2)
	no2=0
	for x in congnosphong2:
		if x.trangthai == False:
			no2+=x.tong
	phong3 = Phong.objects.get(id=3)
	congnosphong3 = Congno.objects.filter(phong=phong3)
	no3=0
	for x in congnosphong3:
		if x.trangthai == False:
			no3+=x.tong
	context = {
		'phong1': phong1,
		'phong2': phong2,
		'phong3': phong3,
		'congnosphong1': congnosphong1,
		'congnosphong2': congnosphong2,
		'congnosphong3': congnosphong3,
		'no1': no1,
		'no2': no2,
		'no3': no3,
	}
	return render(request, 'home.html', context)

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
	request.session.flush()
	phong = Phong.objects.get(id=id)
	phongs = Phong.objects.all()
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
		if "form-time" in request.POST:
			newnam = request.POST['nam']
			newcongnos = getcongnobythangnam(congnos, newnam)
			for x in newcongnos:
				if x.trangthai == False:
					tong = tong + x.tong
			context = {
				'phong': phong,
				'phongs': phongs,
				'congnos': newcongnos,
				'thangnam': thangnam,
				'thang': thang,
				'nam': newnam,
				'nams': nams,
				'tong': tong,
			}
			return render(request, 'phong.html', context)
		if "form-trangthai" in request.POST:
			congnoid = request.POST['congnoid']
			congno = Congno.objects.get(id=congnoid)
			if congno.trangthai == True:
				congno.trangthai = False
			else:
				congno.trangthai = True
			congno.save()
			context = {
				'phong': phong,
				'phongs': phongs,
				'congnos': congnos,
				'thangnam': thangnam,
				'thang': thang,
				'nam': nam,
				'nams': nams,
				'tong': tong,
			}
			# return render(request, 'phong.html', context)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	context = {
				'phong': phong,
				'phongs': phongs,
				'congnos': congnos,
				'thangnam': thangnam,
				'thang': thang,
				'nam': nam,
				'nams': nams,
				'tong': tong,
			}
	return render(request, 'phong.html', context)


		


def getthangtruoc(thang, nam):
	thangtruoc = 0
	namtruoc = 0
	if thang == "1":
		thangtruoc = 12
		namtruoc = int(nam) - 1
	else:
		thangtruoc = int(thang) - 1
		namtruoc = int(nam)
	return str(thangtruoc) + "/" + str(namtruoc)

def tiendiennuoc(congnothangnay, congnothangtruoc):
	sodien = congnothangnay.sodien - congnothangtruoc.sodien
	print(congnothangnay.sodien)
	print(congnothangtruoc.sodien)
	print(sodien)
	sonuoc = congnothangnay.sonuoc - congnothangtruoc.sonuoc
	congnothangnay.tiennuoc = sonuoc*18000
	if sodien > 150:
		congnothangnay.tiendien = (sodien - 150)*3500 + 150*3000
		print("yes")
	else:
		congnothangnay.tiendien = sodien*3000
	print(congnothangnay.tiendien)
	congnothangnay.save()
	return 0

def congnothangchitiet(request, id, thang, nam):
	phong = Phong.objects.get(id=id)
	thangnam = thang + "/" + nam
	congno = Congno.objects.get(phong=phong, thang=thangnam)
	thangtruoc = getthangtruoc(thang, nam)
	congnothangtruoc = Congno.objects.get(phong=phong, thang=thangtruoc)
	tongsodien = congno.sodien - congnothangtruoc.sodien
	tongsonuoc = congno.sonuoc - congnothangtruoc.sonuoc
	tiendiennuoc(congno, congnothangtruoc)
	context = {
		"phong": phong,
		"thangnam": thangnam,
		"congno": congno,
		"congnothangtruoc": congnothangtruoc,
		"tongsodien": tongsodien,
		"tongsonuoc": tongsonuoc,
	}
	return render(request, 'congnothangchitiet.html', context)

def tinhtien(request):
	return render(request, 'tinhtine.html')

def phongcheck(request, id, id2):
	congno = Congno.objects.get(id=id2)
	if request.method == "POST":
		if form.is_valid():
			name = request.POST['name']
			password = request.POST['password']
			if name == "admin" and password == "admin":
				if congno.trangthai == True:
					congno.trangthai = False
				else:
					congno.trangthai = True
	congno.save()
	return render(request, 'check.html')