from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as  BaseUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _


admin.site.site_title = "Abhishek Yadav"
admin.site.site_header = "Abhishek Yadav Administration"
admin.site.index_title = "Abhishek Yadav Administration"


class CountryCodeFormCreate(BaseUserCreationForm):
    class Meta:
        widgets = {
            'mobile_number': PhoneNumberPrefixWidget(initial='IN'),
        }


class CountryCodeFormUpdate(BaseUserChangeForm):
    class Meta:
        widgets = {
            'mobile_number': PhoneNumberPrefixWidget(initial='IN'),
        }


class UserModelAdmin(BaseUserAdmin):
    form = CountryCodeFormUpdate
    add_form = CountryCodeFormCreate
    list_display = ('id', 'username', 'email', 'mobile_number', 'is_active', 'action', 'created_at', 'updated_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups', 'created_at', 'updated_at')
    fieldsets = (
        ('User Credentials', {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'mobile_number', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'mobile_number', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'mobile_number', 'first_name', 'last_name')
    ordering = ('id', 'username', 'email', 'mobile_number', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_per_page = 20
    filter_horizontal = ()
    readonly_fields = ('last_login', 'created_at', 'updated_at')

    def action(self, obj):
        if obj.id:
            return mark_safe("<a class='button btn' style='color:green; padding:0 1rem; ' href='/admin/portfolio/user/{}/change/'>Edit</a>".format(obj.id)
                             + "    " + "<a class='button btn' style='color:red; padding:0 1rem; ' href='/admin/portfolio/user/{}/delete/'>Delete</a>".format(obj.id))
        else:
            social_button = '<a  href="#">---</a>'
            return mark_safe(u''.join(social_button))
admin.site.register(User, UserModelAdmin)