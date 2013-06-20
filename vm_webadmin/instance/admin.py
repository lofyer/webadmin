from django.contrib import admin
from instance.models import VirtualMachine,HardDrive

class HDInline(admin.StackedInline):
	model = HardDrive
	max_num = 10

class VirtualMachineAdmin(admin.ModelAdmin):
	fieldsets = [
		('Basic Infomation', {
			'fields':('vmname', 'createdate', 'useros', 'qemucmd')
		}),
	]
	inlines = [HDInline, ]

admin.site.register(VirtualMachine, VirtualMachineAdmin)
