from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.

def mainPage(request):
    if request.method == 'POST':
        form =  ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            name_phone = f'{name} {phone}'

            recipients = ['befordshir@gmail.com']

            try:
                send_mail(name_phone, comment, 'sunbaking@yandex.ru', recipients)
            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/index.html', {'form':form})
        
    else:
        form = ContactForm()

    return render(request, 'main_page/bootstrap.html', {'form':form})


def mainPage2(request):
    return render(request, 'main_page/index.html')

