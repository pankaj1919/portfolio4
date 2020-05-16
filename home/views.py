from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login')
# def addhome(request):
# 	form = HomeForm()
# 	if request.method == 'POST':
# 		form = HomeForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('addhome')
	
# 	total=Home.objects.all()
# 	context = {'form':form,'total':total}
# 	return render(request, 'Backend/home/addhomepage.html', context)

def addhome(request):
	if request.method == "POST":
		newform = HomeForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addhome')
	else:
		form = HomeForm()

	log_user=request.user
	total=Home.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/home/addhomepage.html',context)


@login_required(login_url='login')
def updatehome(request, pk):

	item = Home.objects.get(id=pk)
	form = HomeForm(instance=item)

	if request.method == 'POST':
		form = HomeForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addhome')

	context = {'form':form}
	return render(request, 'Backend/home/addhomepage.html', context)


@login_required(login_url='login')
def deletehome(request, pk):
	item = Home.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addhome')

	context = {'item':item}
	return render(request, 'Backend/home/homedelete.html', context)