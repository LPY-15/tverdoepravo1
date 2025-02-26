from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main_page'

urlpatterns = [
    path('', views.mainPage, name = 'main_page'),
    path('temp/', views.mainPage2, name = 'main_page2'),
    path('flooding/', views.flooding, name = 'flooding'),
    path('expertise/', views.expertise, name = 'expertise'),
    path('example/', views.example, name = 'example'),
    path('css/styles.css', TemplateView.as_view(
        template_name='styles.css',
        content_type='text/css')
    ),
]