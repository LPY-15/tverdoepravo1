from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

app_name = 'main_page'

urlpatterns = [
    path('', views.mainPage, name = 'main_page'),
    path('temp/', views.mainPage2, name = 'main_page2'),
    path('flooding/', views.flooding, name = 'flooding'),
    path('expertise/', views.expertise, name = 'expertise'),
    path('example/', views.example, name = 'example'),
    path('pre-trial/', views.pre_trial, name = 'pre-trial'),
    path('making-documents/', views.making_documents, name = 'making_documents'),
    path('labor-disputes/', views.labor_disputes, name = 'labor_disputes'),
    path('cancellation/', views.cancellation, name = 'cancellation'),
    path('refusal/', views.refusal, name = 'refusal'),
    path('trademark/', views.trademark, name = 'trademark'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('css/styles.css', TemplateView.as_view(
        template_name='styles.css',
        content_type='text/css')
    ),
]