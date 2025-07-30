from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CancellationFormPage1, CancellationFormPage2, CancellationFormPage3, RefusalFormPage1, RefusalFormPage2, RefusalFormPage3, RefusalFormPage4
from django.template.loader import render_to_string
import logging
logger = logging.getLogger(__name__)
import requests


# Create your views here.
sender = 'befordshir@mail.ru'
recipient = ['befordshir@gmail.com']



def mainPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/main_page.html', {'form':form})
        
    else:

        form = ContactForm()

    return render(request, 'main_page/main_page.html', {'form':form})



def flooding(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
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

            try:
                send_mail(name_phone, comment, sender, recipient)

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

            try:
                send_mail(name_phone, comment, sender, recipient)

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

            try:
                send_mail(name_phone, comment, sender, recipient)

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

            try:
                send_mail(name_phone, comment, sender, recipient)

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

            try:
                send_mail(name_phone, comment, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/labor_disputes.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/labor_disputes.html', {'form': form})



def cancellation(request):

    agreement_form = ContactForm()
    cancellation_form_page1 = CancellationFormPage1()
    cancellation_form_page2 = CancellationFormPage2()
    cancellation_form_page3 = CancellationFormPage3()

    if request.method =='POST':

        agreement_form = ContactForm(request.POST)
        cancellation_form_page1 = CancellationFormPage1(request.POST)
        cancellation_form_page2 = CancellationFormPage2(request.POST)
        cancellation_form_page3 = CancellationFormPage3(request.POST)

        if agreement_form.is_valid():

            try:
                send_mail('1', '1', sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        if cancellation_form_page1.is_valid():

            cleaned = cancellation_form_page1.cleaned_data

            request.session['debtor_name'] = cleaned['debtor_name']
            request.session['debtor_address'] = cleaned['debtor_address']
            request.session['debtor_email'] = cleaned['debtor_email']
            request.session['debtor_phone'] = cleaned['debtor_phone']

        elif cancellation_form_page2.is_valid():

            cleaned = cancellation_form_page2.cleaned_data
            
            request.session['court_type'] = cleaned['court_type']
            request.session['court_name'] = cleaned['court_name']
            request.session['court_address'] = cleaned['court_address']
            request.session['court_order_number'] = cleaned['court_order_number']
            request.session['order_issuing_date'] = str(cleaned['order_issuing_date'])
            request.session['order_receiving_date'] = str(cleaned['order_receiving_date'])
            
        elif cancellation_form_page3.is_valid():
            
            debtor_name = request.session.get('debtor_name')
            debtor_address = request.session.get('debtor_address')
            debtor_email = request.session.get('debtor_email')
            debtor_phone = request.session.get('debtor_phone')

            court_type = request.session.get('court_type')
            court_name = request.session.get('court_name')
            court_address = request.session.get('court_address')
            court_order_number = request.session.get('court_order_number')
            order_issuing_date = request.session.get('order_issuing_date')
            order_receiving_date = request.session.get('order_receiving_date')

            collector_name = cancellation_form_page3.cleaned_data['collector_name']
            collector_address = cancellation_form_page3.cleaned_data['collector_address']
            
            debtor_data = f'{debtor_name} {debtor_address} {debtor_email} {debtor_phone}'
            court_data = f'{court_type} {court_name} {court_address} {court_order_number} {order_issuing_date} {order_receiving_date}'
            collector_data = f'{collector_name} {collector_address}'
            cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'
            
            try:
                send_mail('3step', cancellation_form_data, sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

    return render(request, 'main_page/cancellation.html', {'agreement_form': agreement_form, 'cancellation_form_page1': cancellation_form_page1, 'cancellation_form_page2': cancellation_form_page2, 'cancellation_form_page3': cancellation_form_page3})

        

def refusal(request):
    agreement_form = ContactForm()
    refusal_form_page1 = RefusalFormPage1()
    refusal_form_page2 = RefusalFormPage2()
    refusal_form_page3 = RefusalFormPage3()
    refusal_form_page4 = RefusalFormPage4()

    if request.method =='POST':

        agreement_form = ContactForm(request.POST)
        refusal_form_page1 = RefusalFormPage1(request.POST)
        refusal_form_page2 = RefusalFormPage2(request.POST)
        refusal_form_page3 = RefusalFormPage3(request.POST)
        refusal_form_page4 = RefusalFormPage4(request.POST)

        if agreement_form.is_valid():

            try:
                send_mail('1', '1', sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        if refusal_form_page1.is_valid():

            cleaned = refusal_form_page1.cleaned_data
            request.session['refusal_form_name'] = cleaned['refusal_form_name']
            request.session['refusal_form_email'] = cleaned['refusal_form_email']
            request.session['refusal_form_phone'] = cleaned['refusal_form_phone']


        elif refusal_form_page2.is_valid():

            cleaned = refusal_form_page2.cleaned_data
            request.session['passport_series_and_number'] = cleaned['passport_series_and_number']
            request.session['passport_issue_org'] = cleaned['passport_issue_org']
            request.session['passport_issue_date'] = str(cleaned['passport_issue_date'])
            request.session['declarant_address'] = cleaned['declarant_address']


        elif refusal_form_page3.is_valid():

            cleaned = refusal_form_page3.cleaned_data
            request.session['creditor_name_or_tax_identification_number'] = cleaned['creditor_name_or_tax_identification_number']
            request.session['credit_agreement_number'] = cleaned['credit_agreement_number']
            request.session['creditor_address'] = cleaned['creditor_address']
            request.session['credit_agreement_date'] = str(cleaned['credit_agreement_date'])


        elif refusal_form_page4.is_valid():

            refusal_form_name = request.session.get('refusal_form_name')
            refusal_form_email = request.session.get('refusal_form_email')
            refusal_form_phone = request.session.get('refusal_form_phone')

            passport_series_and_number = request.session.get('passport_series_and_number')
            passport_issue_org = request.session.get('passport_issue_org')
            passport_issue_date = request.session.get('passport_issue_date')
            declarant_address = request.session.get('declarant_address')

            creditor_name_or_tax_identification_number = request.session.get('creditor_name_or_tax_identification_number')
            credit_agreement_number = request.session.get('credit_agreement_number')
            creditor_address = request.session.get('creditor_address')
            credit_agreement_date = request.session.get('credit_agreement_date')

            refusal_form_comment = refusal_form_page4.cleaned_data['refusal_form_comment']
            
            refusal_form_data_page1 = f'{refusal_form_name} {refusal_form_email} {refusal_form_phone}'
            refusal_form_data_page2 = f'{passport_series_and_number} {passport_issue_org} {passport_issue_date} {declarant_address}'
            refusal_form_data_page3 = f'{creditor_name_or_tax_identification_number} {credit_agreement_number} {creditor_address} {credit_agreement_date}'
            refusal_form_data_page4 = f'{refusal_form_comment}'
            refusal_form_data = f'{refusal_form_data_page1} {refusal_form_data_page2} {refusal_form_data_page3} {refusal_form_data_page4}'
            
            try:
                send_mail('4step', refusal_form_data, sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

    return render(request, 'main_page/refusal.html', {'agreement_form': agreement_form, 'refusal_form_page1': refusal_form_page1, 'refusal_form_page2': refusal_form_page2, 'refusal_form_page3': refusal_form_page3, 'refusal_form_page4': refusal_form_page4})



def trademark(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']

            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/trademark.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/trademark.html', {'form': form})

