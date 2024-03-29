from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.forms import RegistrationForm, LoginForm
from random import random

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from good_hands_app.models import Donation

User = get_user_model()

class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
            else:
                return redirect('register')
            return redirect('landing_page')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        ret_val = super().form_valid(form)
        self.object.set_password(form.cleaned_data['pass_1'])
        self.object.save()
        return ret_val

class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        donations = Donation.objects.filter(user=user).order_by('is_taken')
        return render(request, 'user_profile.html', {'donations': donations})

    # def form_valid(self, form):
    #     user = User.objects.create_user(
    #         email=form.cleaned_data['email'],
    #         first_name=form.cleaned_data['first_name'],
    #         last_name=form.cleaned_data['last_name'],
    #         password=form.cleaned_data['pass_1'],
    #         is_active=False,
    #     )
    #     current_site = get_current_site(self.request)
    #     subject = "Aktywacja konta"
    #     message = render_to_string('registration/account_activation_email.html', {
    #         'user': user,
    #         'domain': current_site.domain,
    #         'protocol': 'http',
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': default_token_generator.make_token(user),
    #     })
    #     to_email = form.cleaned_data['email']
    #     email = EmailMessage(
    #         subject, message, to=[to_email]
    #     )
    #     email.send()
    #     # messages.success(self.request, "Użytkownik został pomyślnie zarejestrowany")
    #     return redirect('account_activation_done')



