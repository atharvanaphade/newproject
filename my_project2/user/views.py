from django.shortcuts import render
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user:
			return render(request, 'login.html')
		else:    
		    return render(request, 'home.html', context = {'invalid':"Details Entered are Invalid!"})
	return render(request, 'home.html')


def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		fname = request.POST.get('first_name')
		lname = request.POST.get('last_name')
		email = request.POST.get('email')
		phonenumber = request.POST.get('phonenumber')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password2 == password1 and User.objects.filter(username = username).first() == None:
		  user = User.objects.create_user(username = username, first_name = fname, last_name = lname, email = email, password = password1)
		  Profile.objects.create(user = user, phonenumber = phonenumber)
		  user2 = authenticate(username = username, password = password1)
		  if user2:
		  	return render(request, 'login.html')
		elif(password1 != password2):
			return render(request, 'register.html', context = {'passerror':"Passwords Dont Match!"})
		elif(User.objects.filter(username = username).first() != None):
			return render(request, 'register.html', context = {'usererror':"Username is already taken! Try a different one!"} )

	return render(request, 'register.html')	

@login_required			
def user_login(request):
	if request.method == 'POST':
		logout(request)
		return HttpResponseRedirect(reverse(''))
	return render(request, 'login.html')