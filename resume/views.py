from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
# def addeducation(request):
#     form = EducationForm()
#     if request.method == 'POST':
# 	    form = EducationForm(request.POST)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addeducation')

#     total=resume_study.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/resume/Education/add-education.html', context)

def addeducation(request):
	if request.method == "POST":
		newform = EducationForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addeducation')
	else:
		form = EducationForm()

	log_user=request.user
	total=resume_study.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/resume/Education/add-education.html',context)

@login_required(login_url='login')
def updateeducation(request, pk):

	item = resume_study.objects.get(id=pk)
	form = EducationForm(instance=item)

	if request.method == 'POST':
		form = EducationForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addeducation')

	context = {'form':form}
	return render(request, 'Backend/resume/Education/add-education.html', context)

@login_required(login_url='login')
def deleteeducation(request, pk):
	item = resume_study.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addeducation')

	context = {'item':item}
	return render(request, 'Backend/resume/Education/delete-education.html', context)

@login_required(login_url='login')
# def addwork(request):
#     form = WorkForm()
#     if request.method == 'POST':
# 	    form = WorkForm(request.POST,user=request.user)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addwork')

#     total=work_history.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/resume/Work/add-work.html', context)

def addwork(request):
	if request.method == "POST":
		newform = WorkForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addwork')
	else:
		form = WorkForm()

	log_user=request.user
	total=work_history.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/resume/Work/add-work.html',context)

@login_required(login_url='login')
def updatework(request, pk):

	item = work_history.objects.get(id=pk)
	form = WorkForm(instance=item)

	if request.method == 'POST':
		form = WorkForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addwork')

	context = {'form':form}
	return render(request, 'Backend/resume/Work/add-work.html', context)

@login_required(login_url='login')
def deletework(request, pk):
	item = work_history.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addwork')

	context = {'item':item}
	return render(request, 'Backend/resume/Work/delete-work.html', context)


@login_required(login_url='login')
# def addskill(request):
#     form = SkillForm()
#     if request.method == 'POST':
# 	    form = SkillForm(request.POST,user=request.user)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addskill')

#     total=Skill.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/resume/Soft-Skill/add-skill.html', context)

def addskill(request):
	if request.method == "POST":
		newform = SkillForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addwork')
	else:
		form = SkillForm()

	log_user=request.user
	total=Skill.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/resume/Soft-Skill/add-skill.html',context)


@login_required(login_url='login')
def updateskill(request, pk):

	item = Skill.objects.get(id=pk)
	form = SkillForm(instance=item)

	if request.method == 'POST':
		form = SkillForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addskill')

	context = {'form':form}
	return render(request, 'Backend/resume/Soft-Skill/add-skill.html', context)

@login_required(login_url='login')
def deleteskill(request, pk):
	item = Skill.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addskill')

	context = {'item':item}
	return render(request, 'Backend/resume/Soft-Skill/delete-skill.html', context)


@login_required(login_url='login')
# def addtechnical(request):
#     form = TechnicalForm()
#     if request.method == 'POST':
# 	    form = TechnicalForm(request.POST,user=request.user)
# 	    if form.is_valid():
# 		    form.save()
# 		    return redirect('addtechnical')

#     total=Technical.objects.all()
#     context = {
#         'form':form,
#         'total':total,
#     }
#     return render(request, 'Backend/resume/Technical-Skill/add-technical.html', context)


def addtechnical(request):
	if request.method == "POST":
		newform = TechnicalForm(request.POST)
		if newform.is_valid():
			form = newform.save(commit=False)
			form.author = request.user
			form.save()
		return redirect('addtechnical')
	else:
		form = TechnicalForm()

	log_user=request.user
	total=Technical.objects.filter(author=log_user)
	context = {'form':form,'total':total}
	return render(request, 'Backend/resume/Technical-Skill/add-technical.html',context)

@login_required(login_url='login')
def updatetechnical(request, pk):

	item = Technical.objects.get(id=pk)
	form = TechnicalForm(instance=item)

	if request.method == 'POST':
		form = TechnicalForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addtechnical')

	context = {'form':form}
	return render(request, 'Backend/resume/Technical-Skill/add-technical.html', context)

@login_required(login_url='login')
def deletetechnical(request, pk):
	item = Technical.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addtechnical')

	context = {'item':item}
	return render(request, 'Backend/resume/Technical-Skill/delete-technical.html', context)