from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin




class CustomUserManager(BaseUserManager):
    def create_user(self, username, mobile_number, first_name, last_name, email, password=None):
        if not username:
            raise ValueError('User must have Username')
        if not email:
            raise ValueError('User must have Email')
        if not mobile_number:
            raise ValueError('User must have Mobile Number')
        if not first_name:
            raise ValueError("User must have a First Name")
        if not last_name:
            raise ValueError("User must have a Last Name")
               
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
         mobile_number = mobile_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, mobile_number, first_name, last_name, email, password=None):
        """
        Creates and saves a superuser with the given username, email, first_name, password.
        """
        user = self.create_user(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            mobile_number = mobile_number,
            password = password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user    


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(max_length=100, unique=True, validators=[username_validator], error_messages={'unique': "A user with that username already exists.",})
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mobile_number = PhoneNumberField(max_length=15)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email',  'mobile_number']

    def __str__(self):
        return self.username
    

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class About(BaseModel):
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile')
    description = models.TextField()
    experience = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    projects = models.PositiveIntegerField(validators=[MaxValueValidator(999)])

    def profile_tag(self):
        if self.profile:
            return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.profile.url))
        return None
    profile_tag.short_description = 'Profile'
    profile_tag.allow_tags = True