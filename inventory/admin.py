# Inventory Admin Area for Meander

from django.contrib import admin
from inventory.models import Asset, AssetModel

admin.site.register(AssetModel)
admin.site.register(Asset)
