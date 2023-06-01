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
            'subject': forms.TextInput(attrs={'placeholder':'subject *', 'id':'subjectid'}),
            'message': forms.Textarea(attrs={'placeholder':'Message *', 'id':'messageid'}),
        }
