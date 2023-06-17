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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def profile_tag(self):
        if self.profile:
            return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.profile.url))
        return None
    profile_tag.short_description = 'Profile'
    profile_tag.allow_tags = True


class Resume(BaseModel):
    resume = models.FileField(upload_to='resume')

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'



class CurrentStatus(BaseModel):
    heading = models.CharField(max_length=100) 
    status = models.TextField()

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name = 'Current Status'
        verbose_name_plural = 'Current Status'



class SiteVisitedIPs(BaseModel):
    ip = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    device_type = models.CharField(max_length=100, null=True, blank=True)
    os_type = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.ip
    
    class Meta:
        verbose_name = 'Site Visited IP'
        verbose_name_plural = 'Site Visited IPs'



class AboutDetail(BaseModel):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About Detail'
        verbose_name_plural = 'About Detail'

    def profile_tag(self):
        if self.profile:
            return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.profile.url))
        return None
    profile_tag.short_description = 'Profile'
    profile_tag.allow_tags = True


class Education(BaseModel):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.degree


class Experience(BaseModel):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.company
    

class ContactUs(BaseModel):
    email = models.EmailField(max_length=100, unique=True)
    mobile_number = PhoneNumberField(max_length=15, unique=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class Enquiry(BaseModel):
    name = models.CharField(max_length=100)
    mobile_number = PhoneNumberField(max_length=15)
    email = models.EmailField(max_length=100)
    ip = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    device_type = models.CharField(max_length=100, null=True, blank=True)
    os_type = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'


class Specialization(BaseModel):
    heading = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.heading
    

class SocialProfile(BaseModel):
    PROFILE = [
        ("Linkedin", 'Linkedin'),
        ("Github", 'Github'),
        ("Instagram", 'Instagram'),
        ("Facebook", 'Facebook'),
        ("Twitter", 'Twitter'),
        ("Snapchat", 'Snapchat'),
        ("LeetCode", 'LeetCode'),
        ("HackerRank", 'HackerRank'),
    ]
    heading = models.CharField(max_length=100, choices=PROFILE, unique=True, default='Linkedin')
    url = models.URLField()

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name = 'Social Profile'
        verbose_name_plural = 'Social Profiles'


class Credential(BaseModel):
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile')
    about = models.TextField()

    def __str__(self):
        return self.name

    def profile_tag(self):
        if self.profile:
            return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.profile.url))
        return None
    profile_tag.short_description = 'Profile'
    profile_tag.allow_tags = True


class CredentialEducation(BaseModel):
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.degree
    
    class Meta:
        verbose_name = 'Credential Education'
        verbose_name_plural = 'Credential Educations'


class CredentialExperience(BaseModel):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company
    
    class Meta:
        verbose_name = 'Credential Experience'
        verbose_name_plural = 'Credential Experiences'


class Skill(BaseModel):
    LEVEL = [
        ("Beginner", 'Beginner'),
        ("Intermediate", 'Intermediate'),
        ("Proficient", 'Proficient'),
        ("Expert", 'Expert'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, choices=LEVEL, default='Intermediate')
    percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name
    

class Certificate(BaseModel):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    issue_date = models.DateField()


    def __str__(self):
        return self.name
    

class Work(BaseModel):
    TYPE = [
        ("Web App", 'Web App'),
        ("Mobile App", 'Mobile App'),
        ("Web And Mobile App", 'Web And Mobile App'),
    ]
    name = models.CharField(max_length=100, unique=True)
    app_type = models.CharField(max_length=100, choices=TYPE, default='Web App')
    image_1 = models.ImageField(upload_to='work')
    image_2 = models.ImageField(upload_to='work')
    about = models.TextField()
    skill_description = models.TextField()
    description = models.TextField()
    year = models.CharField(max_length=100)
    client = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def image_tag_1(self):
        if self.image_1:
            return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.image_1.url))
        return None
    image_tag_1.short_description = 'Image'
    image_tag_1.allow_tags = True


