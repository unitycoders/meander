# Inventory Admin Area for Meander

from django.contrib import admin
from inventory.models import System, SystemModel, Peripheral, Accessory

class SystemAdmin(admin.ModelAdmin):
	list_display = ('tag', 'model')
	fieldsets = (
			(None, {
				'fields': ('tag', 'model'),
			}),
			("Vendor Details", {
				'fields': ('serial_number', ),
			})
		)

admin.site.register(System, SystemAdmin)
admin.site.register(SystemModel)

admin.site.register(Peripheral)

class AccessoryAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'stock', 'needs_reorder')

admin.site.register(Accessory, AccessoryAdmin)
