from django.http import HttpResponse
from django.shortcuts import render
from good_hands_app.models import Donation, Institution, Category
# Create your views here.
from django.views.generic import CreateView, View


class LandingPageView(View):
    def get(self, request):
        quantity = sum([donation.quantity for donation in Donation.objects.all()])
        instytutions_donated = Institution.objects.filter(donation__isnull=False).distinct().count()
        instytutions = Institution.objects.all()
        fundations_list = instytutions.filter(type=1)
        non_governmental_list = instytutions.filter(type=2)
        lokal_collection_list = instytutions.filter(type=3)
        return render(request, 'index.html', {
            "quantity": quantity,
            "instytutions_donated": instytutions_donated,
            "fundations_list": fundations_list,
        "non_governmental_list":non_governmental_list,
        "lokal_collection_list":lokal_collection_list})


class AddDonationView(View):
    def get(self, request):
        categories = Category.objects.all()
        instytutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'instytutions': instytutions})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
