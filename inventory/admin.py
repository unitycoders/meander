# Inventory Admin Area for Meander

from django.contrib import admin
from inventory.models import Asset, AssetModel

admin.site.register(AssetModel)

class AssetAdmin(admin.ModelAdmin):
	list_display = ['tag', 'model']
	search_fields = ['tag']

admin.site.register(Asset, AssetAdmin)
