from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
# def addportfolio(request):
#     form = PortfolioForm()
#     if request.method == 'POST':
# 	    form = PortfolioForm(request.POST,request.FILES)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addportfolio')

#     total=portfolio.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, "Backend/portfolio/add-portfolio.html", context)

def addportfolio(request):
	if request.method == "POST":
		newform = PortfolioForm(request.POST,request.FILES)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addportfolio')
	else:
		form = PortfolioForm()

	log_user=request.user
	total=portfolio.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, "Backend/portfolio/add-portfolio.html",context)

@login_required(login_url='login')
def updateportfolio(request, pk):

	item = portfolio.objects.get(id=pk)
	form = PortfolioForm(instance=item)

	if request.method == 'POST':
		form = PortfolioForm(request.POST,request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addportfolio')

	context = {'form':form}
	return render(request, "Backend/portfolio/add-portfolio.html", context)

@login_required(login_url='login')
def deleteportfolio(request, pk):
	item = portfolio.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addportfolio')

	context = {'item':item}
	return render(request, "Backend/portfolio/delete-portfolio.html", context)

@login_required(login_url='login')
# def addcategoryportfolio(request):
#     form = PortfoliocategoryForm()
#     if request.method == 'POST':
# 	    form = PortfoliocategoryForm(request.POST)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addcategoryportfolio')

#     total=Category.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, "Backend/portfolio/category/add-categoryportfolio.html", context)

def addcategoryportfolio(request):
	if request.method == "POST":
		newform = PortfoliocategoryForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addcategoryportfolio')
	else:
		form = PortfoliocategoryForm()

	log_user=request.user
	total=Category.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, "Backend/portfolio/category/add-categoryportfolio.html",context)



@login_required(login_url='login')
def updatecategoryportfolio(request, pk):
	item = Category.objects.get(id=pk)
	form = PortfoliocategoryForm(instance=item)
	if request.method == 'POST':
		form = PortfoliocategoryForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addcategoryportfolio')

	context = {'form':form}
	return render(request, "Backend/portfolio/category/add-categoryportfolio.html", context)

@login_required(login_url='login')
def deletecategoryportfolio(request, pk):
	item = Category.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addcategoryportfolio')

	context = {'item':item}
	return render(request, "Backend/portfolio/category/delete-categoryportfolio.html", context)