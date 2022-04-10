from django.http import HttpResponse
from django.shortcuts import render
from good_hands_app.models import Donation, Institution
# Create your views here.
from django.views.generic import CreateView, View


class LandingPageView(View):
    def get(self, request):
        quantity = sum([donation.quantity for donation in Donation.objects.all()])
        instytutions_donated = Institution.objects.filter(donation__isnull=False).distinct().count()
        instytutions = Institution.objects.all()
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
