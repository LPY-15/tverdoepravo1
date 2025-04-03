from django.shortcuts import render
from django.http import HttpRequest
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.

def mainPage(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

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
            
            return render(request, 'main_page/main_page.html', {'form':form})
        
    else:

        form = ContactForm()

    return render(request, 'main_page/main_page.html', {'form':form})



def mainPage2(request):

    return render(request, 'main_page/index.html')


def flooding(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

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
            
            return render(request, 'main_page/flooding.html', {'form':form})
        
    else:

        form = ContactForm()

    return render(request, 'main_page/flooding.html', {'form':form})


def expertise(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
            
            return render(request, 'main_page/expertise.html', {'form': form})
            
    else:
        form = ContactForm()
    
    return render (request, 'main_page/expertise.html', {'form': form})



def example(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
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
            
            return render(request, 'main_page/example.html', {'form': form})
        
    else:
        form = ContactForm()

    return render(request, 'main_page/example.html', {'form': form})



def pre_trial(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/pre-trial.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/pre-trial.html', {'form': form})

def making_documents(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/making_documents.html', {'form': form})
    
    else:
        form = ContactForm()
    
    return render(request, 'main_page/making_documents.html', {'form': form})



def labor_disputes(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/labor_disputes.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/labor_disputes.html', {'form': form})

def cancellation(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/cancellation.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/cancellation.html', {'form': form})



def refusal(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/refusal.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/refusal.html', {'form': form})



def trademark(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
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
            
        return render(request, 'main_page/trademark.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/trademark.html', {'form': form})

