from .models import *
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404



class IndexView(View):
    def get(self, request):
        ip = request.META.get('REMOTE_ADDR')
        about = About.objects.latest('id')
        return render (request, 'index.html', {'about':about, 'ip':ip})
    


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
        about_detail = AboutDetail.objects.latest('id')
        educations = Education.objects.all().order_by('-id')
        experiences = Experience.objects.all().order_by('-id')
        return render (request, 'about.html', {'about_detail':about_detail, 'educations':educations, 'experiences':experiences})
    


class ContactView(View):
    def get(self, request):
        return render (request, 'contact.html')



class WorksView(View):
    def get(self, request):
        return render (request, 'works.html')
    



class WorkDetailsView(View):
    def get(self, request):
        return render (request, 'work-details.html')
    


class ServiceView(View):
    def get(self, request):
        return render (request, 'service.html')
    


class CredentialsView(View):
    def get(self, request):
        return render (request, 'credentials.html')
    


class BlogView(View):
    def get(self, request):
        return render (request, 'blog.html')
    


class BlogDetailsView(View):
    def get(self, request):
        return render (request, 'blog-details.html')
    

