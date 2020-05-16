from django.shortcuts import render
from .models import AllTasks
from django.http import HttpResponseRedirect

def addtask(request, name):
	content = request.POST['addtask']
	all_tasks = AllTasks(Task=content)
	all_tasks.save()
	return HttpResponseRedirect('/' + name)