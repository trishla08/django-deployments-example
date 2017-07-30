from django.shortcuts import render
from django.contrib.auth.models import User
from app5.models import UserProfileInfo
from app5.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
	return render(request, 'html/index.html')
	
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def profilepage(request, username):
	#user = get_object_or_404(UserProfileInfo, user_username=username)
	#user1 = user.UserProfileInfo

	user = User.objects.get(username=username)
	return render(request, 'html/pp.html', {"user":user,})

def search(request):

	if (request.method == 'POST'):
		proname = request.POST.get('search')

		return redirect('app5:profilepage',username=proname)


def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profilepic' in request.FILES:
				profile.profilepic = request.FILES['profilepic']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'html/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account not active.")

		else:
			print("Someone logged in and failed")
			print("Username: {} and password: {}".format(username, password))
			return HttpResponse("wrong, idiot.")

	else:
		return render(request,'html/login.html', {})

def user_status(request,username):

#	return HttpResponse("wrong, idiot.")

	if request.method == 'POST':
		mystatus = request.POST.get('status')
		user = User.objects.get(username=username)
		profile = user.userprofileinfo
		profile.status = mystatus
		profile.save()
		return redirect('app5:profilepage',username=username)
	    
		#trishla8 mypass8