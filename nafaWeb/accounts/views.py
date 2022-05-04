from django.shortcuts import render, redirect

from accounts.models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from grouping.models import *

#  method to register account


def register_account(request):
    # check if the user is already logged in
    if request.user.is_authenticated:
        return redirect("main:home")

    # if not logged in
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST or None)

            # check if the form is valid
            if form.is_valid():
                user = form.save(commit=False)

                duplicate = False
                nonWarhawks = False
                # for u in users:
                #     if user.email == u.email:
                #         error_message = "Email Already Exists"
                #         duplicate = True
                #         break
                if Profile.objects.filter(email=user.email).exists():
                    duplicate = True

                # duplicate check
                if duplicate:
                    return render(request, 'accounts/register.html', {"error_message": "Email Already Exists", "form": form})

                if nonWarhawks:
                    return render(request, 'accounts/register.html', {"error_message": "You entered non Warhawks Email.", "form": form})

                user.is_active = False

                user.save()

                # create user
                user.refresh_from_db()

                user.copule_with = None
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.maiden_name = request.POST.get("maiden_name")
                user.street_address = request.POST.get(
                    "street_address")
                user.city = request.POST.get("city")
                user.zip = request.POST.get("zipcode")
                user.country_name = request.POST.get("country_name")
                user.graduate_year = request.POST.get("grad_year")

                print(user.first_name)
                user.save()

                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('accounts/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    'protocol': 'http'
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()

                print("Successfully sent email using the sendgrid api")
                return HttpResponse('Please confirm your email address to complete the registration')
                # return redirect("daily:home")
        else:
            form = RegistrationForm(request.POST or None)
        return render(request, 'accounts/register.html', {'form': form})


# activate account
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Profile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        print(e)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        print("Activated Successfully")
        return redirect("main:home")
    else:
        return HttpResponse('Activation link is invalid!')

# login user


def login_user(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            # now we get the data from html templates
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email)
            

            # authenticating the credentials
            user = authenticate(email=email, password=password)
            if user is not None:
                # meaning that the credentials are correct
                print("User is notNone")
                if user.is_active:
                    login(request, user)
                    return redirect("main:home")
                else:
                    return render(request, 'accounts/login.html', {'error-message': 'Your account has not been activated.'})
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Invalid email or Password'})
        return render(request, 'accounts/login.html')

# logout user
# logout


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("accounts:login_user")
    else:
        return redirect("accounts:login_user")



def user_profile(request, uid):
        user = Profile.objects.get(id=uid)
        groups = Group.objects.filter(user= user)[0:3]
        for group in groups:
            print(group)
        context = {"user":user,"groups":groups}
        return render(request, 'accounts/profile.html', context)
    
def edit_profile(request, uid):
        edit_user = Profile.objects.get(id=uid)
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=edit_user)
            if form.is_valid():
                form.save()
            return redirect("accounts:user_profile",uid)
        else:
            form = ProfileForm(instance=edit_user)
        return render(request, 'accounts/editProfile.html', {"form": form, "label": "Edit","userId":uid})