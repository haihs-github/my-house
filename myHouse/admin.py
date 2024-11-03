from django.contrib import admin
from .models import Phong, Congno
# Register your models here.


class PhongAdmin(admin.ModelAdmin):
	list_display = ("id", 'stt', 'vitri', "sodienthangtruoc", "sodienthangnay", "sonuocthangtruoc", "sonuocthangnay", "sodien", "sonuoc", 'tienphong', 'no')

class CongnoAdmin(admin.ModelAdmin):
	list_display = ("id", "thang","sodien", "sonuoc", "tiennuoc", "tiendien", 'tienphong', "trangthai", "tong", "phong")


admin.site.register(Phong, PhongAdmin)
admin.site.register(Congno, CongnoAdmin)