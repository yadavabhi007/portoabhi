from .models import *
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as  BaseUserChangeForm


admin.site.site_title = "Abhishek Yadav"
admin.site.site_header = "Abhishek Yadav Administration"
admin.site.index_title = "Abhishek Yadav Administration"


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))
    

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        widgets = {
            'mobile_number': PhoneNumberPrefixWidget(initial='IN'),
        }

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        widgets = {
            'mobile_number': PhoneNumberPrefixWidget(initial='IN'),
        }

class UserModelAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id', 'username', 'email', 'mobile_number', 'is_active', 'action', 'created_at', 'updated_at')
    list_display_links = ('id', 'username', 'email', 'mobile_number')
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
    list_max_show_all = 10000000
    filter_horizontal = ()
    filter_vertical = ()
    readonly_fields = ('last_login', 'created_at', 'updated_at')

    def action(self, obj):
        if obj.id:
            return mark_safe("<a class='button btn' style='color:green; padding:0 1rem; ' href='/admin/portfolio/user/{}/change/'>Edit</a>".format(obj.id)
                             + "    " + "<a class='button btn' style='color:red; padding:0 1rem; ' href='/admin/portfolio/user/{}/delete/'>Delete</a>".format(obj.id))
        else:
            social_button = '<a  href="#">---</a>'
            return mark_safe(u''.join(social_button))
admin.site.register(User, UserModelAdmin)


# class AdminContactForm(forms.ModelForm):
#     class Meta:
#         widgets = {
#             'phone': PhoneNumberPrefixWidget(initial='IN'),
#         }

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     form = AdminContactForm


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_tag', 'role', 'name', 'created_at', 'updated_at']
    search_fields = ('role', 'name',)
    ordering = ('id', 'role', 'name', 'created_at', 'updated_at')
    list_per_page = 20
    list_max_show_all = 10000000
    filter_horizontal = ()
    list_filter = ['role', 'created_at', 'updated_at']
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


@admin.register(AboutDetail)
class AboutDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile_tag', 'name', 'created_at', 'updated_at']
    search_fields = ('name',)
    ordering = ('id', 'name', 'created_at', 'updated_at')
    list_per_page = 20
    list_max_show_all = 10000000
    filter_horizontal = ()
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ('created_at', 'updated_at')
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }


