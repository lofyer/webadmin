from django.db import models

# Create your models here.
class CommonOptions(models.Model):
	vmname = models.CharField('VM Name',max_length=255)
	createdate = models.DateTimeField('Date created')
    	Linux = 'linux'
	Windows = 'windows'
	Linux_x64 = 'linux_x64'
	Windows_x64 = 'windows_x64'
	OS = (
        (Linux, 'linux'),
	(Windows, 'windows'),
        (Linux_x64, 'linux_x64'),
	(Windows_x64, 'windows_x64'),
	)
    	useros = models.CharField(max_length=64,
                                      choices=OS,
                                      default=Linux_x64)

