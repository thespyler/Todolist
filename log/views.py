from django.shortcuts import render
from .models import Person
from django.http import HttpResponse

names = []
passwords= []
for i in range(10):
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
	# for i in range(10):
	# 	check_n = Person.objects.get(id=i).name
	# 	check_p = Person.objects.get(id=i).password
	# 	if check_n == name and check_p == password:
	# 		return HttpResponse(request, "Hello Abhilash")
	# 	else:
	# 		continue
	# return HttpResponse(request, "Sorry Abhilash")
	return render(request, 'new.html',
				 {'names': names,
			 	 'pass': passwords,
			 	 'name': name,
			 	 'password': password,
			 		})
def new_log(request):
	return render(request, 'signup.html')