from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('addhome')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func



def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'profile':
			return redirect('addhome')

		if group == 'admin':
			return view_func(request, *args, **kwargs)
		else:
			messages.info(request, 'Sorry,This function is for Admin Only' )
			return redirect ('login')

	return wrapper_function