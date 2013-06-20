from django.contrib import admin
from instance.models import CommonOptions

admin.site.register(CommonOptions)

class vmadmin(admin.ModelAdmin):
	list_display=('vmname','createdate')
