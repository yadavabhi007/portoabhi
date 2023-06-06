import socket
from .models import *
from .forms import *
from django.views import View
from django.contrib import messages
from django.http import FileResponse
from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render, redirect



class IndexView(View):
    def get(self, request):
        about = About.objects.first()
        current_status = CurrentStatus.objects.first()
        proxy_servers = request.META.get('HTTP_X_FORWARDED_FOR')
        if request.user_agent.is_mobile:
            device_type = "Mobile"
        elif request.user_agent.is_tablet:
            device_type = "Tablet"
        elif request.user_agent.is_pc:
            device_type = "PC"
        else:
            device_type = "Bot"
        browser_type = request.user_agent.browser.family
        browser_version = request.user_agent.browser.version_string
        os_type = request.user_agent.os.family
        os_version = request.user_agent.os.version_string
        g = GeoIP2()
        if proxy_servers:
            ip = proxy_servers.split(',')[-1]
            try:
                city = g.city(ip)['city']
                country = g.city(ip)['country_name']
            except:
                city = ''
                country = ''
            # SiteVisitedIPs.objects.create(ip=ip, device=socket.gethostname(), device_type=device_type, city=city, country=country, browser_type=browser_type, browser_version=browser_version, os_type=os_type, os_version=os_version)
        else:
            ip = request.META.get('REMOTE_ADDR')
            try:
                city = g.city(ip)['city']
                country = g.city(ip)['country_name']
            except:
                city = ''
                country = ''
            # SiteVisitedIPs.objects.create(ip=ip, device=socket.gethostname(), device_type=device_type, city=city, country=country, browser_type=browser_type, browser_version=browser_version, os_type=os_type, os_version=os_version)
        message = f'You are visiting from'
        message_ip = f'IP: {ip}'
        message_device = f'Device: {socket.gethostname()}'
        message_device_type = f'Device Type: {device_type}'
        message_city = f'City: {city}'
        message_country = f'Country: {country}'
        message_browser_type = f'Browser Type: {browser_type}'
        message_browser_version = f'Browser Version: {browser_version}'
        message_os_type = f'OS Type: {os_type}'
        message_os_version = f'OS Version: {os_version}'
        context = {'about':about, 'ip':ip, 'device':socket.gethostname(), 'device_type':device_type, 'city':city, 'country':country, 'browser_type':browser_type, 'browser_version':browser_version, 'os_type':os_type, 'os_version':os_version, 'message':message, 'message_ip':message_ip, 'message_device':message_device, 'message_device_type':message_device_type, 'message_city':message_city, 'message_country':message_country, 'message_browser_type':message_browser_type, 'message_browser_version':message_browser_version, 'message_os_type':message_os_type, 'message_os_version':message_os_version, 'current_status':current_status}
        return render (request, 'index.html', context)
    


class ResumeView(View):
    def get(self, request):
            try:
                resume = Resume.objects.latest('id')
                return FileResponse(open('media/'+ str(resume.resume), 'rb'), content_type='application/pdf')
            except:
                messages.error(request, 'No File Found')
                return redirect ('index')


class AboutView(View):
    def get(self, request):
        about_detail = AboutDetail.objects.first()
        educations = Education.objects.all().order_by('-id')
        experiences = Experience.objects.all().order_by('-id')
        return render (request, 'about.html', {'about_detail':about_detail, 'educations':educations, 'experiences':experiences})
    


class ContactView(View):
    def get(self, request):
        contact = ContactUs.objects.first()
        forms = EnquiryForm()
        return render (request, 'contact.html', {'contact':contact, 'forms':forms})
    def post(self, request):
        contact = ContactUs.objects.first()
        proxy_servers = request.META.get('HTTP_X_FORWARDED_FOR')
        if request.user_agent.is_mobile:
            device_type = "Mobile"
        elif request.user_agent.is_tablet:
            device_type = "Tablet"
        elif request.user_agent.is_pc:
            device_type = "PC"
        else:
            device_type = "Bot"
        browser_type = request.user_agent.browser.family
        browser_version = request.user_agent.browser.version_string
        os_type = request.user_agent.os.family
        os_version = request.user_agent.os.version_string
        g = GeoIP2()
        if proxy_servers:
            ip = proxy_servers.split(',')[0]
            try:
                city = g.city(ip)['city']
                country = g.city(ip)['country_name']
            except:
                city = None
                country = None
        else:
            ip = request.META.get('REMOTE_ADDR')
            try:
                city = g.city(ip)['city']
                country = g.city(ip)['country_name']
            except:
                city = None
                country = None
        request.POST = request.POST.copy()
        device = socket.gethostname()
        request.POST['ip'] = ip
        request.POST['device'] = device
        request.POST['device_type'] = device_type
        request.POST['city'] = city
        request.POST['country'] = country
        request.POST['browser_type'] = browser_type
        request.POST['browser_version'] = browser_version
        request.POST['os_type'] = os_type
        request.POST['os_version'] = os_version
        forms = EnquiryForm(request.POST)
        if forms.is_valid():
            forms.cleaned_data['ip'] = ip
            forms.cleaned_data['device'] = device
            forms.cleaned_data['device_type'] = device_type
            forms.cleaned_data['city'] = city
            forms.cleaned_data['country'] = country
            forms.cleaned_data['browser_type'] = browser_type
            forms.cleaned_data['browser_version'] = browser_version
            forms.cleaned_data['os_type'] = os_type
            forms.cleaned_data['os_version'] = os_version
            forms.save()
            forms = EnquiryForm()
            messages.success(request, 'Your Message Was Sent Successfully')
            return render (request, 'contact.html', {'contact':contact, 'forms':forms})
        messages.error(request, 'Your Message Was Not Sent')
        return render (request, 'contact.html', {'contact':contact, 'forms':forms})



class WorksView(View):
    def get(self, request):
        return render (request, 'works.html')
    



class WorkDetailsView(View):
    def get(self, request):
        return render (request, 'work-details.html')
    


class SpecializationView(View):
    def get(self, request):
        specializations = Specialization.objects.all().order_by('-id')
        return render (request, 'specialization.html', {'specializations':specializations})
    


class CredentialsView(View):
    def get(self, request):
        return render (request, 'credentials.html')
    



