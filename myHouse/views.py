from django.shortcuts import render, redirect
from .models import Phong, Congno
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	print(request.session.get('login', False))
	context = {
		'checklogin': request.session.get('login', False)
	}
	return redirect('/check', context)

def home(request):
	checklogin = request.session.get('login', False)
	phongs = Phong.objects.all()
	for x in phongs:
		congnos = Congno.objects.filter(phong=x)
		for i in congnos:
			if i.trangthai == False:
				x.no += i.tong
	context = {
		'phongs': phongs,
		'checklogin': checklogin,
	}
	return render(request, 'home.html', context)

def getthangnam(): # mm/yyyy
	thang = datetime.now().month
	year = datetime.now().year
	return str(thang) + "/" + str(year)

def getthangtruoc(thang, nam):
	gformruoc = 0
	namtruoc = 0
	if thang == "1":
		thangtruoc = 12
		namtruoc = int(nam) - 1
	else:
		thangtruoc = int(thang) - 1
		namtruoc = int(nam)
	return str(thangtruoc) + "/" + str(namtruoc)

def getnam(thang): # yyyy
	tmp = thang.split('/')
	return tmp[1]

def getcongnobythangnam(congnos, date):
	newcongnos = list()
	for x in congnos:
		if date in x.thang:
			newcongnos.append(x)
	return newcongnos

def phong(request, stt):
	checklogin = request.session.get('login', False)
	phong = Phong.objects.get(stt=stt)
	phongs = Phong.objects.all()
	congnos = Congno.objects.filter(phong=phong).order_by("-id")
	thangnam = getthangnam() #mm/yyyy
	thang = int(datetime.now().month)
	nam = int(datetime.now().year)
	nams = list()
	tong = 0
	for x in congnos:
		if x.trangthai == False:
			tong += x.tong
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
				'checklogin': checklogin,
			}
			return render(request, 'phong.html', context)
		if "form-trangthai" in request.POST:
			if request.session.get('login', False) == False:
				return redirect('/')
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
				'checklogin': checklogin,
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
				'checklogin': checklogin,
			}
	return render(request, 'phong.html', context)

def tiendiennuoc(congnothangnay, congnothangtruoc):
	sodien = congnothangnay.sodien - congnothangtruoc.sodien
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

def congnothangchitiet(request, stt, thang, nam):
	phong = Phong.objects.get(stt=stt)
	thangnam = thang + "/" + nam
	congno = Congno.objects.get(phong=phong, thang=thangnam)
	thangtruoc = getthangtruoc(thang, nam)
	congnothangtruoc = Congno()
	try:
		congnothangtruoc = Congno.objects.get(phong=phong, thang=thangtruoc)
		print('co thang truoc:', congnothangtruoc.thang)
	except:
		try:
			for x in Congno.objects.filter(phong=phong).order_by('-id'):
				if datetime.strptime(x.thang, '%m/%Y') < datetime.strptime(thangnam, '%m/%Y'):
					congnothangtruoc = x
					print('thang gan nhat la:', congnothangtruoc)
					break
		except:
			congnothangtruoc = Congno(thang=thangtruoc, tienphong= phong.tienphong, sodien=0, sonuoc=0, tiennuoc=0, tiendien=0, trangthai=True, phong=phong)
			# congnothangtruoc = Congno.objects.get(phong=phong, thang=thangnam)
			print('ko co thang truoc:', congnothangtruoc)
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
		'checklogin': request.session.get('login', False)
	}
	return render(request, 'congnothangchitiet.html', context)

def tinhtien(request):
	if request.session.get('login', False) == False:
		return redirect('/')
	thang = getthangnam()
	phongs = list(Phong.objects.all().order_by('stt'))
	if request.method == "POST":
		thangform = request.POST['thang']
		tmp = thangform.split('/')
		thangnay = tmp[0]
		namnay = tmp[1]
		for x in phongs:
			Congno()
			sodien = float(request.POST[f'sodienp{x.id}'])
			sonuoc = float(request.POST[f'sonuocp{x.id}'])
			congno = Congno(thang=thangform, sodien=sodien, sonuoc=sonuoc, trangthai=False, phong=x)
			congnothangtruoc = Congno()
			try:
				congnothangtruoc = Congno.objects.get(phong=x, thang=thangform)
				print('co thang truoc:', congnothangtruoc.thang)
			except:
				try:
					for i in Congno.objects.filter(phong=x).order_by('-id'):
						if datetime.strptime(i.thang, '%m/%Y') < datetime.strptime(thangform, '%m/%Y'):
							congnothangtruoc = i
							print('thang gan nhat la:', congnothangtruoc)
							break
				except:
					congnothangtruoc = Congno(thang=getthangtruoc(thangnay, namnay), tienphong= x.tienphong, sodien=0, sonuoc=0, tiennuoc=0, tiendien=0, trangthai=True, phong=x)
			print('congnothangtruoc.sodien:',congnothangtruoc.sodien)
			print('congnothangnay.sodien:',congno.sodien)
			tiendiennuoc(congno, congnothangtruoc)
			x.sodienthangtruoc = x.sodienthangnay
			x.sonuocthangtruoc = x.sonuocthangnay
		return redirect('home')
	context = {
		'thang': thang,
		'checklogin': request.session.get('login', False),
		'phongs': phongs,
	}
	return render(request, 'tinhtien.html', context)

def check(request):
	if request.method == "POST":
		name = request.POST['name']
		password = request.POST['password']
		if name == "admin" and password == "admin":
			request.session['login'] = True
			return redirect('home')
		else:
			request.session['login'] = False
			request.session.flush()
			return redirect('home')
	return render(request, 'check.html')

def dangxuat(request):
	request.session.flush()
	return redirect('check')
