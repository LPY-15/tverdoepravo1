from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main_page'

urlpatterns = [
    path('', views.mainPage, name = 'main_page'),
    path('temp/', views.mainPage2, name = 'main_page2'),
    path('css/styles.css', TemplateView.as_view(
        template_name='styles.css',
        content_type='text/css')
    ),
]