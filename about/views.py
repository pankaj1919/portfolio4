from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
# def addintro(request):
# 	form = AboutForm()
# 	if request.method == 'POST':
# 		form = AboutForm(request.POST,request.FILES,request.user)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('addintro')

# 	total=About.objects.filter(author=request.user)
# 	context = {
#         'form':form,
# 		'total':total,
# 	}
# 	return render(request, 'Backend/aboutme/Intro/add-intro.html', context)

def addintro(request):
	if request.method == "POST":
		newform = AboutForm(request.POST,request.FILES)
		if newform.is_valid():
			new = newform.save(commit=False)
			new.author = request.user
			new.save()
		return redirect('addintro')
	else:
		new = AboutForm()

	log_user=request.user
	total=About.objects.filter(author=log_user)
	context = {'new':new,'total':total}
	return render(request, 'Backend/aboutme/Intro/add-intro.html',context)

@login_required(login_url='login')
def updateintro(request, pk):

	item = About.objects.get(id=pk)
	form = AboutForm(instance=item)

	if request.method == 'POST':
		form = AboutForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addintro')

	context = {'form':form}
	return render(request, 'Backend/aboutme/Intro/add-intro.html', context)

@login_required(login_url='login')
def deleteintro(request, pk):
	item = About.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addintro')

	context = {'item':item}
	return render(request, 'Backend/aboutme/Intro/delete-intro.html', context)

@login_required(login_url='login')
# def addservice(request):
#     form = ServiceForm()
#     if request.method == 'POST':
# 	    form = ServiceForm(request.POST)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addservice')

#     total=Service.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/aboutme/service/service-add.html', context)

def addservice(request):
	if request.method == "POST":
		newform = ServiceForm(request.POST,request.FILES)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addservice')
	else:
		form = ServiceForm()

	log_user=request.user
	total=Service.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/aboutme/service/service-add.html',context)

@login_required(login_url='login')
def updateservice(request, pk):

	item = Service.objects.get(id=pk)
	form = ServiceForm(instance=item)

	if request.method == 'POST':
		form = ServiceForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addservice')

	context = {'form':form}
	return render(request, 'Backend/aboutme/service/service-add.html', context)

@login_required(login_url='login')
def deleteservice(request, pk):
	item = Service.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addservice')

	context = {'item':item}
	return render(request, 'Backend/aboutme/service/service-delete.html', context)

@login_required(login_url='login')
# def addclient(request):
#     form = ClientForm()
#     if request.method == 'POST':
# 	    form = ClientForm(request.POST,request.FILES)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addclient')

#     total=Client.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/aboutme/client/addclient.html', context)

def addclient(request):
	if request.method == "POST":
		newform = ClientForm(request.POST,request.FILES)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addclient')
	else:
		form = ClientForm()

	log_user=request.user
	total=Client.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/aboutme/client/addclient.html',context)

@login_required(login_url='login')
def updateclient(request, pk):

	item = Client.objects.get(id=pk)
	form = ClientForm(instance=item)

	if request.method == 'POST':
		form = ClientForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addclient')

	context = {'form':form}
	return render(request, 'Backend/aboutme/client/addclient.html', context)


@login_required(login_url='login')
def deleteclient(request, pk):
	item = Client.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addclient')

	context = {'item':item}
	return render(request, 'Backend/aboutme/client/delete-client.html', context)


@login_required(login_url='login')
# def addfact(request):
#     form = FactForm()
#     if request.method == 'POST':
# 	    form = FactForm(request.POST)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addfact')

#     total=Facts.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/aboutme/facts/addfact.html', context)

def addfact(request):
	if request.method == "POST":
		newform = FactForm(request.POST,request.FILES)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addfact')
	else:
		form = FactForm()

	log_user=request.user
	total=Facts.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/aboutme/facts/addfact.html',context)

@login_required(login_url='login')
def updatefact(request, pk):

	item = Facts.objects.get(id=pk)
	form = FactForm(instance=item)

	if request.method == 'POST':
		form = FactForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addfact')

	context = {'form':form}
	return render(request, 'Backend/aboutme/facts/addfact.html', context)


@login_required(login_url='login')
def deletefact(request, pk):
	item = Facts.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addfact')

	context = {'item':item}
	return render(request, 'Backend/aboutme/facts/delete-fact.html', context)


@login_required(login_url='login')
# def addtestomonial(request):
#     form = ProfileForm()
#     if request.method == 'POST':
# 	    form = ProfileForm(request.POST,request.FILES)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addtestomonial')

#     total=Profile.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/aboutme/testomonials/addtestomonial.html', context)


def addtestomonial(request):
	if request.method == "POST":
		newform = ProfileForm(request.POST,request.FILES)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addtestomonial')
	else:
		form = ProfileForm()

	log_user=request.user
	total=Profile.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/aboutme/testomonials/addtestomonial.html',context)


@login_required(login_url='login')
def updatetestomonial(request, pk):

	item = Profile.objects.get(id=pk)
	form = ProfileForm(instance=item)

	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addtestomonial')

	context = {'form':form}
	return render(request, 'Backend/aboutme/testomonials/addtestomonial.html', context)


@login_required(login_url='login')
def deletetestomonial(request, pk):
	item = Profile.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addtestomonial')

	context = {'item':item}
	return render(request, 'Backend/aboutme/testomonials/deletetestomonial.html', context)