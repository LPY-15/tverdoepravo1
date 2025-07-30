from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields import BLANK_CHOICE_DASH

class HiddenPlaceholderSelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if option['value'] == '':
            option['attrs']['disabled'] = True
            option['attrs']['hidden'] = True
        return option

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    comment = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}))

court_type_list = [
    ('', "Тип суда"),
    ("1", "Мировой суд"),
    ("2", "Арбитражный суд"),
]

class CancellationFormPage1(forms.Form):
    debtor_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО должника (кому был выдан)', 'id': 'debtor_name'}))
    debtor_address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес должника (по прописке)', 'id': 'debtor_address'}))
    debtor_email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'id': 'debtor_email'}))
    debtor_phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон', 'id': 'debtor_phone'}))


class CancellationFormPage2(forms.Form):
    court_type = forms.ChoiceField(choices=court_type_list, required=True, widget=HiddenPlaceholderSelect(attrs={'class': 'form-control', 'placeholder': 'Полное наименование судебного участка', 'id': 'court_type'}))
    court_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полное наименование судебного участка', 'id': 'court_name'}))
    court_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полный адрес судебного участка', 'id': 'court_address'}))
    court_order_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер судебного приказа (судебного дела, производства)', 'id': 'court_order_number'}))
    order_issuing_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата получения судебного приказа', 'id': 'order_receiving_date'}))
    order_receiving_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата получения судебного приказа', 'id': 'order_receiving_date'}))


class CancellationFormPage3(forms.Form):
    collector_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование взыскателя', 'id': 'collector_name'}))
    collector_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес взыскателя', 'id': 'collector_address'}))

class RefusalFormPage1(forms.Form):
    refusal_form_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО', 'id': 'refusal_form_name'}))
    refusal_form_email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'id': 'refusal_form_email'}))
    refusal_form_phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон', 'id': 'refusal_form_phone'}))

class RefusalFormPage2(forms.Form):
    passport_series_and_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Серия и номер паспорта', 'id': 'passport_series_and_number'}))
    passport_issue_org = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кем выдан паспорт', 'id': 'passport_issue_org'}))
    passport_issue_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата выдачи паспорта', 'id': 'passport_issue_date', 'class': 'flatpickr_calendar'}))
    declarant_address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес проживания заявителя', 'id': 'declarant_address'}))

class RefusalFormPage3(forms.Form):
    creditor_name_or_tax_identification_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование кредитора или ИНН', 'id': 'creditor_name_or_tax_identification_number'}))
    credit_agreement_number = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер кредитного договора', 'id': 'credit_agreement_number'}))
    creditor_address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес кредитора', 'id': 'creditor_address'}))
    credit_agreement_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата кредитного договора  ', 'id': 'credit_agreement_date', 'class': 'flatpickr_calendar'}))

class RefusalFormPage4(forms.Form):
    refusal_form_comment = forms.CharField(max_length=500, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'id': 'refusal_form_comment'}))
