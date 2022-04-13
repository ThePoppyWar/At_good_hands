from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.forms import RegistrationForm

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


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
