from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from todo_list.models import *
names = []
passwords = []

for i in range(len(Person.objects.all())+1):
	try:
		x = Person.objects.get(id=i).name
		y = Person.objects.get(id=i).password
		names.append(x)
		passwords.append(y)

	except:
		continue


def main(request):
	return render(request, 'login.html')


def check(request):
	name = request.POST['Username']
	password = request.POST['Password']
	likes = str(Likes.objects.get(id=1).likes)
	return render(request, 'new.html',
				 {'names': names,
			 	  'pass': passwords,
			 	  'name': name,
			 	  'password': password,
			 	   'like': likes,
			 	  },)
def new_log(request):
	return render(request, 'signup.html')

def signin(request):
	name = request.POST['name']
	password = request.POST['pass']
	new_person = Person()
	new_person.name = name
	new_person.password = password
	new_person.save()
	try:
		return HttpResponseRedirect('/')
	except:
		return HttpResponse(request, 'Sorry, plz try again')

def addlike(request):
	likem = Likes.objects.get(id=1)
	like = Likes.objects.get(id=1).likes
	like += 1
	likem.save()
	return HttpResponseRedirect('/')

def function(request, name):
	return render(request, 'todo.html',
				 {'name':name,
				   'all_items': AllTasks().objects.all()
				   })