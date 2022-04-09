from django.contrib.auth.models import User
from django.db import models


# Create your models here.

TYPE_FUNDATION = (
    (1, "fundation"),
    (2, "non-governmental organization "),
    (3, "lokal collection"),
    (4, "lokal collection"),
)


class Category(models.Model):
    name = models.CharField(max_length=30)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField()
    type = models.IntegerField(choices=TYPE_FUNDATION, default=1)
    categories = models.ManyToManyField(Category, blank=True)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField()
    phone_number = models.IntegerField()
    city = models.CharField()
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField(auto_now=False)
    pick_up_comment = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


