from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

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
        paginator_fund = Paginator(fundations_list, 5)
        page = request.GET.get('page', 1)
        try:
            fundations_list = paginator_fund.page(page)
        except PageNotAnInteger:
            fundations_list = paginator_fund.page(1)
        except EmptyPage:
            fundations_list = paginator_fund.page(paginator_fund.num_pages)

        paginator_non_gov = Paginator(non_governmental_list, 5)
        page = request.GET.get('page', 1)
        try:
            non_governmental_list = paginator_non_gov.page(page)
        except PageNotAnInteger:
            non_governmental_list = paginator_non_gov.page(1)
        except EmptyPage:
            non_governmental_list = paginator_non_gov.page(paginator_non_gov.num_pages)

        paginator_local = Paginator(lokal_collection_list, 5)
        page = request.GET.get('page', 1)
        try:
            lokal_collection_list = paginator_local.page(page)
        except PageNotAnInteger:
            lokal_collection_list = paginator_local.page(1)
        except EmptyPage:
            lokal_collection_list = paginator_local.page(paginator_local.num_pages)


        return render(request, 'index.html', {
            "quantity": quantity,
            "instytutions_donated": instytutions_donated,
            "fundations_list": fundations_list,
        "non_governmental_list":non_governmental_list,
        "lokal_collection_list":lokal_collection_list})



class AddDonationView(LoginRequiredMixin,View):
    def get(self, request):
        categories = Category.objects.all()
        instytutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories, 'instytutions': instytutions})

    def post(self, request):
        user = request.user
        organization_id = request.POST['organization']
        organization = Institution.objects.get(pk=organization_id)
        quantity = request.POST['bags']
        address = request.POST['address']
        phone_number = request.POST['phone']
        city = request.POST['city']
        zip_code = request.POST['postcode']
        pick_up_date=request.POST['data']
        pick_up_time = request.POST['time']
        pick_up_comment = request.POST['more_info']
        donation = Donation.objects.create(
            quantity=quantity,
            institution=organization,
            address=address,
            phone_number=phone_number,
            city=city,
            zip_code=zip_code,
            pick_up_date=pick_up_date,
            pick_up_time=pick_up_time,
            pick_up_comment=pick_up_comment,
            user=user,
        )
        category_ids= request.POST.getlist('categories')
        categories = Category.objects.filter(id__in=category_ids)
        donation.categories.set(categories)
        donation.save()

        subject = "Potwierdzenie przekazania darowizny"
        message = render_to_string('donation_form_confirmation_emali.html',{
            'user': user,
            "quality": quantity,
            'organization': organization,
            'address': address,
            'zip_code': zip_code,
            'city': city,
            'pick_up_date': pick_up_date,
            'pick_up_time': pick_up_time
        })






