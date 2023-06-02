from django import forms
from .models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MobileNumberForm(forms.ModelForm):
    class Meta:
        widgets = {
            'mobile_number': PhoneNumberPrefixWidget(initial='IN'),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name *', 'id':'nameid'}),
            'mobile_number': PhoneNumberPrefixWidget(initial='IN', attrs={'placeholder':'Mobile Number *', 'id':'mobile_numberid'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email *', 'id':'emailid'}),
            'ip': forms.HiddenInput(attrs={'placeholder':'IP', 'id':'ipid'}),
            'device': forms.HiddenInput(attrs={'placeholder':'Device', 'id':'deviceid'}),
            'device_type': forms.HiddenInput(attrs={'placeholder':'Device Type', 'id':'device_typeid'}),
            'city': forms.HiddenInput(attrs={'placeholder':'City', 'id':'cityid'}),
            'country': forms.HiddenInput(attrs={'placeholder':'Country', 'id':'countryid'}),
            'browser_type': forms.HiddenInput(attrs={'placeholder':'Browser Type', 'id':'browser_typeid'}),
            'browser_version': forms.HiddenInput(attrs={'placeholder':'Browser Version', 'id':'browser_versionid'}),
            'os_type': forms.HiddenInput(attrs={'placeholder':'OS Type', 'id':'os_typeid'}),
            'os_version': forms.HiddenInput(attrs={'placeholder':'OS Version', 'id':'os_versionid'}),
            'subject': forms.TextInput(attrs={'placeholder':'Subject *', 'id':'subjectid'}),
            'message': forms.Textarea(attrs={'placeholder':'Message *', 'id':'messageid'}),
        }
