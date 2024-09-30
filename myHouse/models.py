from django.db import models

# Create your models here.

class Phong(models.Model):
	sodienthangtruoc = models.FloatField(default=0)
	sonuocthangtruoc = models.FloatField(default=0)
	sodienthangnay = models.FloatField(default=sodienthangtruoc)
	sonuocthangnay = models.FloatField(default=sonuocthangtruoc)
	@property
	def sodien(self):
		return int(self.sodienthangnay - self.sodienthangtruoc)
	@property
	def sonuoc(self):
		return int(self.sonuocthangnay - self.sonuocthangtruoc)

class Congno(models.Model):
	thang = models.CharField(max_length=255)
	sodien = models.FloatField(default=0)
	sonuoc = models.FloatField(default=0)
	tiennuoc = models.FloatField(default=0)
	tiendien = models.FloatField(default=0)
	trangthai = models.BooleanField(default=False)
	phong = models.ForeignKey(Phong, on_delete=models.PROTECT, related_name='phong')
	@property
	def tong(self):
		return self.tiennuoc + self.tiendien


