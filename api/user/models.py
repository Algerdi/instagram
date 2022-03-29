from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


def upload_to(instance, filename):
    return f'posts/{filename}'


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, name, password, **other_fields)

    def create_user(self, email, user_name, name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to=upload_to, blank=True,
                               null=True, default='posts/default.jpg')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    bio = models.TextField(max_length=500, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'name']

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("get_user", kwargs={'pk': self.pk})
