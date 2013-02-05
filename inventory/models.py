from django.db import models

class AssetModel(models.Model):
	summary = models.CharField(max_length=150)
	vendor = models.CharField(max_length=250)
	friendly_name = models.CharField(max_length=255)
	barcode_name = models.CharField(max_length=255)

class Asset(models.Model):
	tag = models.CharField(max_length=10, primary_key=True)
	model = models.ForeignKey(AssetModel)

