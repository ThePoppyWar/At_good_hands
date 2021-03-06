# Generated by Django 3.2.12 on 2022-04-20 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'fundation'), (2, 'non-governmental organization '), (3, 'lokal collection')], default=1)),
                ('categories', models.ManyToManyField(blank=True, to='good_hands_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField()),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.DateField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(blank=True, to='good_hands_app.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good_hands_app.institution')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
