from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CancellationFormPage1, CancellationFormPage2, CancellationFormPage3, RefusalFormPage1, RefusalFormPage2, RefusalFormPage3
from django.template.loader import render_to_string
import logging
logger = logging.getLogger(__name__)
import requests
from honeypot.decorators import check_honeypot
from django.contrib import messages

sender = 'befordshir@mail.ru'
recipient = ['tverdoepravo@mail.ru']

def mainPage(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/main_page.html', {'contact_form': contact_form})
        
    else:

        contact_form = ContactForm()

    return render(request, 'main_page/main_page.html', {'contact_form': contact_form})



def flooding(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/flooding.html', {'contact_form':contact_form})
        
    else:

        contact_form = ContactForm()

    return render(request, 'main_page/flooding.html', {'contact_form':contact_form})



def expertise(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/expertise.html', {'contact_form': contact_form})
            
    else:
        contact_form = ContactForm()
    
    return render (request, 'main_page/expertise.html', {'contact_form': contact_form})



def example(request):
    if request.method =='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
            return render(request, 'main_page/example.html', {'contact_form': contact_form})
        
    else:
        contact_form = ContactForm()

    return render(request, 'main_page/example.html', {'contact_form': contact_form})



def pre_trial(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/pre-trial.html', {'contact_form': contact_form})
    
    else:
        contact_form = ContactForm()

    return render(request, 'main_page/pre-trial.html', {'contact_form': contact_form})



def making_documents(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/making_documents.html', {'contact_form': contact_form})
    
    else:
        contact_form = ContactForm()
    
    return render(request, 'main_page/making_documents.html', {'contact_form': contact_form})



def labor_disputes(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/labor_disputes.html', {'contact_form': contact_form})
    
    else:
        contact_form = ContactForm()

    return render(request, 'main_page/labor_disputes.html', {'contact_form': contact_form})



def cancellation(request):

    contact_form = ContactForm()
    cancellation_form_page1 = CancellationFormPage1()
    cancellation_form_page2 = CancellationFormPage2()
    cancellation_form_page3 = CancellationFormPage3()


    if request.method =='POST':

        contact_form = ContactForm(request.POST)
        cancellation_form_page1 = CancellationFormPage1(request.POST)
        cancellation_form_page2 = CancellationFormPage2(request.POST)
        cancellation_form_page3 = CancellationFormPage3(request.POST)

        if contact_form.is_valid():

            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        if cancellation_form_page1.is_valid():

            cleaned = cancellation_form_page1.cleaned_data

            request.session['debtor_name'] = cleaned['debtor_name']
            request.session['debtor_address'] = cleaned['debtor_address']
            request.session['debtor_email'] = cleaned['debtor_email']
            request.session['debtor_phone'] = str(cleaned['debtor_phone'])

        if cancellation_form_page2.is_valid():

            cleaned = cancellation_form_page2.cleaned_data
            
            request.session['court_type'] = cleaned['court_type']
            request.session['court_name'] = cleaned['court_name']
            request.session['court_address'] = cleaned['court_address']
            request.session['court_order_number'] = cleaned['court_order_number']
            request.session['order_issuing_date'] = str(cleaned['order_issuing_date'])
            request.session['order_receiving_date'] = str(cleaned['order_receiving_date'])
            
        if cancellation_form_page3.is_valid():
            
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
            court_data = f'{court_type} {court_name} {court_address} qwe{court_order_number} {order_issuing_date} {order_receiving_date}'
            collector_data = f'{collector_name} {collector_address}'
            cancellation_contact_form_data = f'{debtor_data} {court_data} {collector_data}'

            
            try:
                send_mail('Заявление об отмене судебного приказа', cancellation_contact_form_data, sender, recipient)
                request.session.flush()

            except BadHeaderError:
                return HttpResponse('Invalid header found')

    return render(request, 'main_page/cancellation.html', {'contact_form': contact_form, 'cancellation_form_page1': cancellation_form_page1, 'cancellation_form_page2': cancellation_form_page2, 'cancellation_form_page3': cancellation_form_page3})

        

def refusal(request):
    contact_form = ContactForm()
    refusal_form_page1 = RefusalFormPage1()
    refusal_form_page2 = RefusalFormPage2()
    refusal_form_page3 = RefusalFormPage3()

    if request.method =='POST':

        contact_form = ContactForm(request.POST)
        refusal_form_page1 = RefusalFormPage1(request.POST)
        refusal_form_page2 = RefusalFormPage2(request.POST)
        refusal_form_page3 = RefusalFormPage3(request.POST)

        if contact_form.is_valid():

            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

        if refusal_form_page1.is_valid():

            cleaned = refusal_form_page1.cleaned_data
            request.session['refusal_form_name'] = cleaned['refusal_form_name']
            request.session['refusal_form_email'] = cleaned['refusal_form_email']
            request.session['refusal_form_phone'] = cleaned['refusal_form_phone']
            


        if refusal_form_page2.is_valid():
            
            cleaned = refusal_form_page2.cleaned_data
            request.session['passport_series_and_number'] = cleaned['passport_series_and_number']
            request.session['passport_issue_org'] = cleaned['passport_issue_org']
            request.session['passport_issue_date'] = str(cleaned['passport_issue_date'])
            request.session['declarant_address'] = cleaned['declarant_address']
            


        if refusal_form_page3.is_valid():
            print(refusal_form_page3.errors)

            refusal_form_name = request.session.get('refusal_form_name')
            refusal_form_email = request.session.get('refusal_form_email')
            refusal_form_phone = request.session.get('refusal_form_phone')

            passport_series_and_number = request.session.get('passport_series_and_number')
            passport_issue_org = request.session.get('passport_issue_org')
            passport_issue_date = request.session.get('passport_issue_date')
            declarant_address = request.session.get('declarant_address')

            refusal_contact_form_data_page1 = f' ФИО: {refusal_form_name}, e-mail: {refusal_form_email}, телефон: {refusal_form_phone},'
            refusal_contact_form_data_page2 = f' серия и номер паспорта: {passport_series_and_number}, кем выдан паспорт: {passport_issue_org}, дата выдачи паспорта: {passport_issue_date}, адрес проживания заявителя: {declarant_address}, '

            session_data = request.session.get('creditors_list', [])

            cleaned = refusal_form_page3.cleaned_data
            creditor = {
                'Наименование кредитора или ИНН': cleaned['creditor_name_or_tax_identification_number'],
                'Номер кредитного договора': cleaned['credit_agreement_number'],
                'Адрес кредитора': cleaned['creditor_address'],
                'Дата кредитного договора': str(cleaned['credit_agreement_date'])
            }

            session_data.append(creditor)
            request.session['creditors_list'] = session_data



            if request.POST.get('3_page_submit') == 'clicked':

                creditors_info = '\n'.join(
                    [f"{i+1}. Наименование кредитора или ИНН: {c['Наименование кредитора или ИНН']}, Номер кредитного договора: {c['Номер кредитного договора']}, Адрес кредитора: {c['Адрес кредитора']}, Дата кредитного договора: {c['Дата кредитного договора']}" for i, c in enumerate(session_data)]
                )
                refusal_contact_form_data = f"{refusal_contact_form_data_page1} {refusal_contact_form_data_page2}\n\nКредиторы:\n{creditors_info}"

                try:
                    send_mail('Заявление об отказе от взаимодействия с кредитором', refusal_contact_form_data, sender, recipient)
                    request.session['creditors_list'] = []
                    request.session.flush()


                except BadHeaderError:
                    return HttpResponse('Invalid header found')

    return render(request, 'main_page/refusal.html', {'contact_form': contact_form, 'refusal_form_page1': refusal_form_page1, 'refusal_form_page2': refusal_form_page2, 'refusal_form_page3': refusal_form_page3})



def trademark(request):
    if request.method =='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f' Имя: {name}, телефон: {phone}, комментарий: {comment}'

            try:
                send_mail('Форма обратной связи', name_phone, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/trademark.html', {'contact_form': contact_form})
    
    else:
        contact_form = ContactForm()

    return render(request, 'main_page/trademark.html', {'contact_form': contact_form})

