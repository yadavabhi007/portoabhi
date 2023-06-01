import socket
from .models import *
from .forms import *
from django.views import View
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect



class IndexView(View):
    def get(self, request):
        about = About.objects.latest('id')
        # proxy_servers = request.META.get('HTTP_X_FORWARDED_FOR')
        # if proxy_servers:
        #     ip = proxy_servers.split(',')[-1]
        #     SiteVisitedIPs.objects.create(ip=ip, device=socket.gethostname())
        # else:
        #     ip = request.META.get('REMOTE_ADDR')
        #     SiteVisitedIPs.objects.create(ip=ip, device=socket.gethostname())
        return render (request, 'index.html', {'about':about})
    


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
        if proxy_servers:
            ip = proxy_servers.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        request.POST = request.POST.copy()
        request.POST['ip'] = ip
        device = socket.gethostname()
        request.POST['device'] = device
        forms = EnquiryForm(request.POST)
        if forms.is_valid():
            forms.cleaned_data['ip'] = ip
            forms.cleaned_data['device'] = device
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
    


class SkillsView(View):
    def get(self, request):
        return render (request, 'skills.html')
    


class CredentialsView(View):
    def get(self, request):
        return render (request, 'credentials.html')
    


class BlogView(View):
    def get(self, request):
        return render (request, 'blog.html')
    


class BlogDetailsView(View):
    def get(self, request):
        return render (request, 'blog-details.html')
    

