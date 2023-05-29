from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import *



class IndexView(View):
    def get(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        return render (request, 'index.html')
    


class AboutView(View):
    def get(self, request):
        return render (request, 'about.html')
    


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
    

