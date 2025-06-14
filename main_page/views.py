from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CancellationFormPage1, CancellationFormPage2, CancellationFormPage3
from formtools.wizard.views import CookieWizardView, NamedUrlCookieWizardView
from django.template.loader import render_to_string
import logging
logger = logging.getLogger(__name__)


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

class CancellationWizardView(NamedUrlCookieWizardView):
    
    form_list = [CancellationFormPage1, CancellationFormPage2, CancellationFormPage3]
    template_name = 'main_page/cancellation.html'

    '''def render_next_step(self, form, **kwargs):
        """
        Override this to customize AJAX response for the next step.
        """
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Render only the form part as HTML
            html = render_to_string('main_page/cancellation.html', {'form': form})
            return HttpResponse('1')
            #return JsonResponse({'form_html': html})
        else:
            # fallback for normal POST
            return HttpResponse('2')
            #return super().render_next_step(form, **kwargs)'''
        

    def done(self, form_list, **kwargs):
        try:
            send_mail('5', '4', sender, recipient)

        except BadHeaderError:
            return HttpRequest('Invalid header found')
        
        return HttpResponse('123')


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

        if cancellation_form_page3.is_valid():

            debtor_name = request.POST.get('debtor_name')
            debtor_address = request.POST.get('debtor_address')
            debtor_email = request.POST.get('debtor_email')
            debtor_phone = request.POST.get('debtor_phone')
            debtor_data = f'{debtor_name} {debtor_address} {debtor_email} {debtor_phone}'
            court_type = request.POST.get('court_type')
            court_name = request.POST.get('court_name')
            court_address = request.POST.get('court_address')
            court_order_number = request.POST.get('court_order_number')
            order_issuing_date = request.POST.get('order_issuing_date')
            order_receiving_date = request.POST.get('order_receiving_date')
            court_data = f'{court_type} {court_name} {court_address} {court_order_number} {order_issuing_date} {order_receiving_date}'
            collector_name = cancellation_form_page3.cleaned_data['collector_name']
            collector_address = cancellation_form_page3.cleaned_data['collector_address']
            collector_data = f'Наименование взыскателя: {collector_name}, адрес взыскателя: {collector_address}'
            cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'

            try:
                send_mail(debtor_name, court_address, sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

            print("AJAX POST received!")   # Or use logging
            logger.info("AJAX POST received!")
            # rest of your code...
            # send email or process form
            return JsonResponse({'success': True})
            

            if cancellation_form_page2.is_valid(): 

                court_type = request.POST.get('court_type')
                court_name = request.POST.get('court_name')
                court_address = request.POST.get('court_address')
                court_order_number = request.POST.get('court_order_number')
                order_issuing_date = request.POST.get('order_issuing_date')
                order_receiving_date = request.POST.get('order_receiving_date')
                court_data = f'{court_type} {court_name} {court_address} {court_order_number} {order_issuing_date} {order_receiving_date}'
                
                
                if cancellation_form_page3.is_valid():

                    collector_name = cancellation_form_page3.cleaned_data['collector_name']
                    collector_address = cancellation_form_page3.cleaned_data['collector_address']
                    collector_data = f'Наименование взыскателя: {collector_name}, адрес взыскателя: {collector_address}'
                    cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'


                    try:
                        send_mail('123', '123', sender, recipient)

                    except BadHeaderError:
                        return HttpResponse('Invalid header found')

                    print("AJAX POST received!")   # Or use logging
                    logger.info("AJAX POST received!")
                    # rest of your code...
                    # send email or process form
                    return JsonResponse({'success': True})
                

        
            '''if '1_page_submit' in request.POST:

            try:
                send_mail('123', '123', sender, recipient)

            except BadHeaderError:
                return HttpResponse('Invalid header found')'''

            '''cancellation_form_page1 = CancellationFormPage1(request.POST)
            cancellation_form_page2 = CancellationFormPage2(request.POST)
            cancellation_form_page3 = CancellationFormPage3(request.POST)

            debtor_data = cancellation_form_page1.cleaned_data'''



                #if cancellation_form_page2.is_valid() and cancellation_form_page1.is_valid() and cancellation_form_page3.is_valid():

            '''debtor_name = cancellation_form_page1.cleaned_data
                debtor_name2 = cancellation_form_page2.cleaned_data
                debtor_name3 = cancellation_form_page3.cleaned_data
                debtor_name4 = f'{debtor_name} {debtor_name2} {debtor_name3}'
                debtor_address = cancellation_form_page1.cleaned_data['debtor_address']
                debtor_email = cancellation_form_page1.cleaned_data['debtor_email']
                debtor_phone = cancellation_form_page1.cleaned_data['debtor_phone']'''

                
            '''if cancellation_form_page2.is_valid():

                    court_type = cancellation_form_page2.cleaned_data['court_type']
                    court_name = cancellation_form_page2.cleaned_data['court_name']
                    court_address = cancellation_form_page2.cleaned_data['court_address']
                    court_order_number = cancellation_form_page2.cleaned_data['court_order_number']
                    order_issuing_date = cancellation_form_page2.cleaned_data['order_issuing_date']
                    order_receiving_date = cancellation_form_page2.cleaned_data['order_receiving_date']

                    if cancellation_form_page3.is_valid():

                        collector_name = cancellation_form_page3.cleaned_data['collector_name']
                        collector_address = cancellation_form_page3.cleaned_data['collector_address']
                        debtor_data = f'Имя должника: {debtor_name}, адрес должника: {debtor_address}, e-mail должника: {debtor_email}, телефон должника: {debtor_phone}'
                        court_data = f'Тип суда: {court_type}, полное наименование судебного участка: {court_name}, полный адрес судебного участка: {court_address}, номер судебнго приказа:{court_order_number}, дата вынесения судебнго приказа: {order_issuing_date}, дата получения судебноого приказа: {order_receiving_date}'
                        collector_data = f'Наименование взыскателя: {collector_name}, адрес взыскателя: {collector_address}'
                        cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'

                        try:
                            send_mail(collector_name, collector_address, sender, recipient)

                        except BadHeaderError:
                            return HttpResponse('Invalid header found')'''
            


            #cancellation_form_page1 = CancellationFormPage1(request.POST)
            '''cancellation_form_page2 = CancellationFormPage2(request.POST)
            cancellation_form_page3 = CancellationFormPage3(request.POST)'''

            ''' if cancellation_form_page1.is_valid():
                debtor_name = cancellation_form_page1.cleaned_data['debtor_name']
                debtor_address = cancellation_form_page1.cleaned_data['debtor_address']
                debtor_email = cancellation_form_page1.cleaned_data['debtor_email']
                debtor_phone = cancellation_form_page1.cleaned_data['debtor_phone']'''
            '''court_type = cancellation_form_page2.cleaned_data['court_type']
                court_name = cancellation_form_page2.cleaned_data['court_name']
                court_address = cancellation_form_page2.cleaned_data['court_address']
                court_order_number = cancellation_form_page2.cleaned_data['court_order_number']
                order_issuing_date = cancellation_form_page2.cleaned_data['order_issuing_date']
                order_receiving_date = cancellation_form_page2.cleaned_data['order_receiving_date']
                collector_name = cancellation_form_page3.cleaned_data['collector_name']
                collector_address = cancellation_form_page3.cleaned_data['collector_address']'''

                #debtor_data = f'debtor_name, debtor_address, debtor_email, debtor_phone'
            '''court_data = f'Тип суда: {court_type}, полное наименование судебного участка: {court_name}, полный адрес судебного участка: {court_address}, номер судебнго приказа:{court_order_number}, дата вынесения судебнго приказа: {order_issuing_date}, дата получения судебноого приказа: {order_receiving_date}'
                collector_data = f'Наименование взыскателя: {collector_name}, адрес взыскателя: {collector_address}'
                cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'''


        '''elif 'submit_page_2' in request.POST:

            cancellation_form_page2 = CancellationFormPage2(request.POST)

            if cancellation_form_page2.is_valid():
                court_type = cancellation_form_page2.cleaned_data['court_type']
                court_name = cancellation_form_page2.cleaned_data['court_name']
                court_address = cancellation_form_page2.cleaned_data['court_address']
                court_order_number = cancellation_form_page2.cleaned_data['court_order_number']
                order_issuing_date = cancellation_form_page2.cleaned_data['order_issuing_date']
                order_receiving_date = cancellation_form_page2.cleaned_data['order_receiving_date']

                court_data = f'court_type, court_name, court_address, court_order_number, order_issuing_date, order_receiving_date'

                try:
                    send_mail(debtor_data, '4', sender, recipient)

                except BadHeaderError:
                    return HttpRequest('Invalid header found')''' 

        '''elif 'submit_page_3' in request.POST:

            cancellation_form_page3 = CancellationFormPage3(request.POST)

            if cancellation_form_page3.is_valid():
                collector_name = cancellation_form_page3.cleaned_data['collector_name']
                collector_address = cancellation_form_page3.cleaned_data['collector_address']

                collector_data = [collector_name, collector_address]  
                try:
                    send_mail('5', '4', sender, recipient)

                except BadHeaderError:
                    return HttpRequest('Invalid header found')   '''   
            
        #debtor_data = f'Имя должника: {debtor_name}, адрес должника: {debtor_address}, e-mail должника: {debtor_email}, телефон должника: {debtor_phone}'
        #court_data = f'Тип суда: {court_type}, полное наименование судебного участка: {court_name}, полный адрес судебного участка: {court_address}, номер судебнго приказа:{court_order_number}, дата вынесения судебнго приказа: {order_issuing_date}, дата получения судебноого приказа: {order_receiving_date}'
        #collector_data = f'Наименование взыскателя: {collector_name}, адрес взыскателя: {collector_address}'
        #cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'

        ''' if 'cancellation_submit' in request.POST:
                    cancellation_form_data = f'{debtor_data} {court_data} {collector_data}'
                    try:
                        send_mail('5', '4', sender, recipient)

                    except BadHeaderError:
                        return HttpRequest('Invalid header found')'''


    return render(request, 'main_page/cancellation.html', {'agreement_form': agreement_form, 'cancellation_form_page1': cancellation_form_page1, 'cancellation_form_page2': cancellation_form_page2, 'cancellation_form_page3': cancellation_form_page3})

        

def refusal(request):
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

            try:
                send_mail(name_phone, comment, sender, recipient)

            except BadHeaderError:
                return HttpRequest('Invalid header found')
            
        return render(request, 'main_page/trademark.html', {'form': form})
    
    else:
        form = ContactForm()

    return render(request, 'main_page/trademark.html', {'form': form})

