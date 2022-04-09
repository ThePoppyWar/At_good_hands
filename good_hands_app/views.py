from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'index.html')

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
