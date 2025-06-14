from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from .forms import CancellationFormPage1, CancellationFormPage2, CancellationFormPage3
from .views import CancellationWizardView

app_name = 'main_page'

'''named_contact_forms = (
    ('1_step', CancellationFormPage1),
    ('2_step', CancellationFormPage2),
    ('3_step', CancellationFormPage3),
)
cancellation_wizard = CancellationWizardView.as_view(named_contact_forms,
    url_name='cancellation_step')'''



urlpatterns = [
    path('', views.mainPage, name = 'main_page'),
    path('flooding/', views.flooding, name = 'flooding'),
    path('expertise/', views.expertise, name = 'expertise'),
    path('example/', views.example, name = 'example'),
    path('pre-trial/', views.pre_trial, name = 'pre-trial'),
    path('making-documents/', views.making_documents, name = 'making_documents'),
    path('labor-disputes/', views.labor_disputes, name = 'labor_disputes'),
    #re_path(r'^cancellation/(?P<step>.+)/$', cancellation_wizard, name='cancellation_step'),
    #path('cancellation/', cancellation_wizard, name = 'cancellation'),
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