from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True


    def create_user(self, **kwargs):

        user = self.model(
            **kwargs
        )

        user.set_password(kwargs.get("password", ""))
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(
            **kwargs
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(verbose_name='first_name', max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)

    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin