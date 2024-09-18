from django.contrib import admin
from .models import Phong, Congno
# Register your models here.


class PhongAdmin(admin.ModelAdmin):
	list_display = ("id", "sodienthangtruoc", "sodienthangnay", "sonuocthangtruoc", "sonuocthangnay", "sodien", "sonuoc")

class CongnoAdmin(admin.ModelAdmin):
	list_display = ("id", "thang", "tiennuoc", "tiendien", "trangthai", "tong", "phong")


admin.site.register(Phong, PhongAdmin)
admin.site.register(Congno, CongnoAdmin)