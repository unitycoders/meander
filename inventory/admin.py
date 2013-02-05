# Inventory Admin Area for Meander

from django.contrib import admin
from inventory.models import System, SystemModel, Peripheral, PeripheralModel, Accessory

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

	# Don't allow editing of the PK after creation
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['tag']
		else:
			return []

admin.site.register(System, SystemAdmin)

class SystemModelAdmin(admin.ModelAdmin):
	fieldsets = (
			(None, { 'fields': ('manufacturer', 'product_name')}),
			("Advanced", { 'classes':('collapse',),'fields': ('sku_number', 'family')})
	)

admin.site.register(SystemModel, SystemModelAdmin)

class PeripheralModelAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'total')
admin.site.register(PeripheralModel, PeripheralModelAdmin)

class PeripheralAdmin(admin.ModelAdmin):
	fields = ('tag', 'model')
	list_display = ('tag', 'model')

	# Don't allow editing of the PK after creation
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['tag']
		else:
			return []
admin.site.register(Peripheral, PeripheralAdmin)

class AccessoryAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'stock', 'needs_reorder')
	list_editable = ('stock',)
admin.site.register(Accessory, AccessoryAdmin)
