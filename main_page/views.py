from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm, CancellationFormPage1, CancellationFormPage2, CancellationFormPage3
from formtools.wizard.views import CookieWizardView



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

class CancellationWizardView(CookieWizardView):
    
    form_list = [CancellationFormPage1, CancellationFormPage2, CancellationFormPage3]
    template_name = 'main_page/cancellation.html'

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
        if 'agreement_submit' in request.POST:
            agreement_form = ContactForm(request.POST)

            if agreement_form.is_valid():
                name = agreement_form.cleaned_data['name']
                phone = agreement_form.cleaned_data['phone']
                comment = agreement_form.cleaned_data['comment']

                name_phone = f'{name} {phone}'

                try:
                    send_mail(name_phone, comment, sender, recipient)

                except BadHeaderError:
                    return HttpRequest('Invalid header found')
                
            return render(request, 'main_page/cancellation.html', {'form': agreement_form})
        
        elif 'submit_page_1' in request.POST:

            cwv = CancellationWizardView.as_view()
            CancellationWizardView.as_view()

            return cwv(request)


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

