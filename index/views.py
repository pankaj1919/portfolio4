from django.shortcuts import render,redirect
from about .models import *
from contact .models import *
from home .models import *
from portfolioo .models import *
from resume .models import *
from about .urls import *
from user .models import *


from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, admin_only
from django.views import View

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from .tokens import activation_token

from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.contrib import messages

from contactforms.forms import ContactForm

def index(request):
    forms=ContactForm()
    log_user = request.user
    categorys=Category.objects.all()
    cat=portfolio.objects.all()
    total=Home.objects.filter(author=log_user).first()
    about=About.objects.filter(author=log_user)
    service=Service.objects.filter(author=log_user)
    client=Client.objects.filter(author=log_user)
    fact=Facts.objects.filter(author=log_user)
    profile=Profile.objects.filter(user=log_user)
    resume=resume_study.objects.filter(author=log_user)
    work=work_history.objects.filter(author=log_user)
    skill=Skill.objects.filter(author=log_user)
    technical=Technical.objects.filter(author=log_user)
    contact=Contact.objects.filter(author=log_user)
    context={
        'about':about,
        'total':total,
        'service':service,
        'client':client,
        'fact':fact,
        'profile':profile,
        'resume':resume,
        'work':work,
        'skill':skill,
        'technical':technical,
        'contact':contact,
        'categorys':categorys,
        'cat':cat,
        'forms':forms,
    }
    return render(request, "Frontend/layout/layout.html",context)




class RegisterPageView(View):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        template_name = "register/register.html"
        return render(request, template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            subject = "Activate your account"
            domain_url = get_current_site(request)
            message = render_to_string(
                "Backend/accounts/activation_message.html",
                {
                    "domain": domain_url.domain,
                    "user": user,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": activation_token.make_token(user),
                },
            )
            to_email = form.cleaned_data.get('email')
            send_mail(subject, message, 'punky19161916@gmail.com', [to_email])
            activation_msg = "Open your email to activate account."
            return render(
                request, "Backend/accounts/activate_email.html", {"activation_msg": activation_msg}
            )
        
        template_name = 'register/register.html'
        return render(request, template_name, {"form": form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        # login(request, user)
        return redirect('login')
    else:
        return render(request, "Backend/accounts/activation_fail.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('addintro')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('addintro')
            else:
                messages.info(request, 'Username and Password Does not Match')

        context = {}
        return render(request, 'login/login.html', context)
    
def logoutUser(request):
	logout(request)
	return redirect('login')


