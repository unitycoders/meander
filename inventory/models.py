from django.db import models

##
# This is loosly based on SMBIOS spec as then we can scrape some of the data from the PC :)
#
# The system is devided into three different 'types' of asset.
#
# Systems (laptops, desktops, servers)
# Peripheral (Scanners, Monitors, etc...) - Stuff which is tracked individually
# Accessories (Keyboards, Mice, Leads, ect...) - Stuff which knowing stock levels is useful, but not worth tracking individually
##

##
# Abstract Base classes for the Inventory
# These make sure that Peripherals and Systems behave consistantly with each other.
##

class BaseModel(models.Model):
	manufacturer = models.CharField(max_length=255) # must be non-null
	product_name = models.CharField(max_length=255) # must be non-null

	def __unicode__(self):
		return self.manufacturer + " " + self.product_name

	class Meta:
		abstract = True

class BaseAsset(models.Model):
	tag = models.CharField(max_length=255, primary_key=True)

	class Meta:
		abstract = True

##
# Systems
#
# Computers, Network Equipment and other Core IT stuff. These are tracked indvidually though
# the inventory system and may have support contracts and software licences.
##
class SystemModel(BaseModel):
	sku_number = models.CharField(max_length=255, blank=True, null=True, help_text="A number which uniquly idenfies this configuration (eg. nc2400#abu).")
	family = models.CharField(max_length=255, blank=True, null=True, help_text="The family of products this unit it from (eg. Compaq 6200 Pro series)")

	def __unicode__(self):
		return "%s %s" % (self.manufacturer, self.product_name)

class System(BaseAsset):
	serial_number = models.CharField(max_length=255, blank=True, null=True)
	uuid = models.CharField(max_length=255, blank=True, null=True)
	model = models.ForeignKey(SystemModel)

	def __unicode__(self):
		return "%s" % (self.tag,)

##
# Peripherals are 'dumb' IT equipment which won't usually respond to network scans
# they don't have software management but can have support contracts. They are asset
# tagged and tracked like systems.
##
class PeripheralModel(BaseModel):
	
	def total(self):
		return self.peripheral_set.count()

class Peripheral(BaseAsset):
	model = models.ForeignKey(PeripheralModel)

	def __unicode__(self):
		return self.tag

##
# Accessories
# Arn't indivually tracked, they mearly have a stock level. This category is mostly for alerting IT staff
# that they need to order more when stocks run low or to allow the IT staff to get a summary of IT stocks "at a glance".
##
class Accessory(BaseModel):
	stock = models.PositiveIntegerField()
	minimum = models.PositiveIntegerField()

	def needs_reorder(self):
		return self.stock <= self.minimum

	def __unicode__(self):
		return self.manufacturer + " " + self.product_name

	class Meta:
		verbose_name_plural = "accessories"
