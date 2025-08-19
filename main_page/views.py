from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CancellationFormPage1, CancellationFormPage2, CancellationFormPage3, RefusalFormPage1, RefusalFormPage2, RefusalFormPage3, RefusalFormPage4
from django.template.loader import render_to_string
import logging
logger = logging.getLogger(__name__)
import requests
from honeypot.decorators import check_honeypot
from django.contrib import messages
from django.forms import formset_factory
from django.forms import BaseFormSet, ValidationError


sender = 'befordshir@mail.ru'
recipient = ['befordshir@gmail.com']

class RequiredFormsFormSet(BaseFormSet):
        def clean(self):
            super().clean()
            if any(self.errors):
                return

            filled_forms = 0
            for form in self.forms:
                if form.has_changed():
                    filled_forms += 1
                    # Check required fields manually if needed, but normally form.is_valid() does this
                    for name, field in form.fields.items():
                        if field.required and not form.cleaned_data.get(name):
                            raise ValidationError(f"Поле {field.label or name} обязательно для заполнения.")

            if filled_forms == 0:
                raise ValidationError("Пожалуйста, заполните хотя бы одну форму с данными.")


def mainPage(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")


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
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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

            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
    submit_success_message = f'123'


    if request.method =='POST':

        contact_form = ContactForm(request.POST)
        cancellation_form_page1 = CancellationFormPage1(request.POST)
        cancellation_form_page2 = CancellationFormPage2(request.POST)
        cancellation_form_page3 = CancellationFormPage3(request.POST)

        if contact_form.is_valid():

            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            cancellation_contact_form_data = f'{debtor_data} {court_data} {collector_data}'

            
            try:
                send_mail('3step', cancellation_contact_form_data, sender, recipient)
                messages.success(request, "Form submitted successfully!")

            except BadHeaderError:
                return HttpResponse('Invalid header found')

    return render(request, 'main_page/cancellation.html', {'contact_form': contact_form, 'cancellation_form_page1': cancellation_form_page1, 'cancellation_form_page2': cancellation_form_page2, 'cancellation_form_page3': cancellation_form_page3})

        

def refusal(request):
    contact_form = ContactForm()
    refusal_form_page1 = RefusalFormPage1()
    refusal_form_page2 = RefusalFormPage2()
    refusal_form_page3 = RefusalFormPage3()
    refusal_form_page4 = RefusalFormPage4()
    RefusalFormSetPage3 = formset_factory(RefusalFormPage3, formset=RequiredFormsFormSet, extra=1)
    refusal_formset_page_3 = RefusalFormSetPage3()

    if request.method =='POST':

        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        contact_form = ContactForm(request.POST)
        refusal_form_page1 = RefusalFormPage1(request.POST)
        refusal_form_page2 = RefusalFormPage2(request.POST)
        refusal_form_page3 = RefusalFormPage3(request.POST)
        refusal_form_page4 = RefusalFormPage4(request.POST)
        refusal_formset_page_3 = RefusalFormSetPage3(request.POST)

        if contact_form.is_valid():

            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

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
            


        elif refusal_formset_page_3.is_valid():

            refusal_form_name = request.session.get('refusal_form_name')
            refusal_form_email = request.session.get('refusal_form_email')
            refusal_form_phone = request.session.get('refusal_form_phone')

            passport_series_and_number = request.session.get('passport_series_and_number')
            passport_issue_org = request.session.get('passport_issue_org')
            passport_issue_date = request.session.get('passport_issue_date')
            declarant_address = request.session.get('declarant_address')


            refusal_contact_form_data_page1 = f' ФИО: {refusal_form_name}, e-mail: {refusal_form_email}, телефон: {refusal_form_phone},'
            refusal_contact_form_data_page2 = f' серия и номер паспорта: {passport_series_and_number}, кем выдан паспорт: {passport_issue_org}, дата выдачи паспорта: {passport_issue_date}, адрес проживания заявителя: {declarant_address}, '


            refusal_contact_form_data = f"{refusal_contact_form_data_page1} {refusal_contact_form_data_page2} "


            page3_data = []
            for form in refusal_formset_page_3.forms:
                cleaned = form.cleaned_data
                creditor = {
                    'Наименование кредитора или ИНН': cleaned['creditor_name_or_tax_identification_number'],
                    'Номер кредитного договора': cleaned['credit_agreement_number'],
                    'Адрес кредитора': cleaned['creditor_address'],
                    'Дата кредитного договора': str(cleaned['credit_agreement_date'])
                }
                page3_data.append(creditor)

            # Save to session (or DB if needed)
            session_data = request.session.get('creditors_list', [])
            session_data.extend(page3_data)
            request.session['creditors_list'] = session_data

            refusal_contact_form_data = f"{refusal_contact_form_data_page1} {refusal_contact_form_data_page2} {session_data}"


            if is_ajax:
                return JsonResponse({'status': 'ok', 'saved_data': session_data})

            if refusal_formset_page_3.is_valid() and request.POST.get('3_page_submit') == 'clicked':

                request.session['creditors_list'] = []

                try:
                    send_mail('refusalform', refusal_contact_form_data, sender, recipient)
                    messages.success(request, "Form submitted successfully!")

                except BadHeaderError:
                    return HttpResponse('Invalid header found')
            
            else:
                # Return errors if AJAX
                if is_ajax:
                    errors = refusal_formset_page_3.errors  # list of dicts per form
                    return JsonResponse({'status': 'error', 'errors': errors})

    return render(request, 'main_page/refusal.html', {'contact_form': contact_form, 'refusal_form_page1': refusal_form_page1, 'refusal_form_page2': refusal_form_page2, 'refusal_formset_page_3': refusal_formset_page_3})


    '''elif refusal_form_page4.is_valid():

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

            refusal_contact_form_comment = refusal_form_page4.cleaned_data['refusal_form_comment']
            
            refusal_contact_form_data_page1 = f'{refusal_form_name} {refusal_form_email} {refusal_form_phone}'
            refusal_contact_form_data_page2 = f'{passport_series_and_number} {passport_issue_org} {passport_issue_date} {declarant_address}'
            refusal_contact_form_data_page3 = f'{creditor_name_or_tax_identification_number} {credit_agreement_number} {creditor_address} {credit_agreement_date}'
            refusal_contact_form_data_page4 = f'{refusal_contact_form_comment}'
            refusal_contact_form_data = f'{refusal_contact_form_data_page1} {refusal_contact_form_data_page2} {refusal_contact_form_data_page3} {refusal_contact_form_data_page4}'
            
            try:
                send_mail('4step', refusal_contact_form_data, sender, recipient)
                messages.success(request, "Form submitted successfully!")

            except BadHeaderError:
                return HttpResponse('Invalid header found')

    return render(request, 'main_page/refusal.html', {'contact_form': contact_form, 'refusal_form_page1': refusal_form_page1, 'refusal_form_page2': refusal_form_page2, 'refusal_form_page3': refusal_form_page3, 'refusal_form_page4': refusal_form_page4})
'''


def trademark(request):
    if request.method =='POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            phone = contact_form.cleaned_data['phone']
            comment = contact_form.cleaned_data['comment']

            name_phone = f'{name} {phone}'

            try:
                send_mail(name_phone, comment, sender, recipient)
                messages.success(request, "Form submitted successfully!")

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/trademark.html', {'contact_form': contact_form})
    
    else:
        contact_form = ContactForm()

    return render(request, 'main_page/trademark.html', {'contact_form': contact_form})

