from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, LoginForm

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


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
                return HttpResponse('You not pass. Login or password is not correct')
            return redirect('landing_page')


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
