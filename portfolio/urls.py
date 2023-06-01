from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('resume', views.ResumeView.as_view(), name='resume'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('work-details/', views.WorkDetailsView.as_view(), name='work-details'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('credentials/', views.CredentialsView.as_view(), name='credentials'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-details/', views.BlogDetailsView.as_view(), name='blog-details'),
]