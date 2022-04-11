from django.contrib.auth.models import User
from django.db import models


# Create your models here.

TYPE_FUNDATION = (
    (1, "fundation"),
    (2, "non-governmental organization "),
    (3, "lokal collection"),
)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f' {self.name} '

class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=TYPE_FUNDATION, default=1)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return f"{self.name}"

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Worki:{self.quantity} dla {self.institution}"
