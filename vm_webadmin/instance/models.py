from django.db import models

# Create your models here.
class VirtualMachine(models.Model):
	#VM name
	vmname = models.CharField('VM Name', max_length=255)
	#VM create date
	createdate = models.DateTimeField('Date Created')
	#VM OS(user define)
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
    	useros = models.CharField("Predefined OS", max_length=255, choices=OS, default=Linux_x64)
	#qemu command
	qemucmd = models.CharField("Qemu Command", max_length=255, default='qemu-x86_64-spice')

class HardDrive(models.Model):
	VirtualMachine = models.ForeignKey(VirtualMachine)
	hdcmd = models.CharField("Hard Drive", max_length=255, default='-hda')
	hddevice = models.CharField("Hard Drive Device", max_length=255, default='')
