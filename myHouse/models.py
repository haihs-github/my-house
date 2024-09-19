from django.db import models

# Create your models here.

class Phong(models.Model):
	sodienthangtruoc = models.BigIntegerField(default=0)
	sonuocthangtruoc = models.BigIntegerField(default=0)
	sodienthangnay = models.BigIntegerField(default=sodienthangtruoc)
	sonuocthangnay = models.BigIntegerField(default=sonuocthangtruoc)
	@property
	def sodien(self):
		return int(self.sodienthangnay - self.sodienthangtruoc)
	@property
	def sonuoc(self):
		return int(self.sonuocthangnay - self.sonuocthangtruoc)

class Congno(models.Model):
	thang = models.CharField(max_length=255)
	tiennuoc = models.BigIntegerField(default=0)
	tiendien = models.BigIntegerField(default=0)
	trangthai = models.BooleanField(default=False)
	phong = models.ForeignKey(Phong, on_delete=models.PROTECT, related_name='phong')
	sodien = models.BigIntegerField(default=0)
	sonuoc = models.BigIntegerField(default=0)
	@property
	def tong(self):
		return self.tiennuoc + self.tiendien


