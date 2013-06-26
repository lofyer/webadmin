# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from instance.models import VirtualMachine

def index(request):
	listvm = VirtualMachine.objects.order_by('vmname')[:5]
	context = {'listvm': listvm}
	return render(request, 'instance/index.html', context)

def detail(request, VirtualMachine_id):
	showvm = get_object_or_404(VirtualMachine, pk=VirtualMachine_id)
	return render(request, 'instance/detail.html', {'showvm': showvm})
