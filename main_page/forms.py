from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models.fields import BLANK_CHOICE_DASH

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    comment = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}))

court_type_list = [
    ('', "Тип суда"),
    ("2", "Мировой суд"),
    ("3", "Арбитражный суд"),
]

class CancellationFormPage1(forms.Form):
    debtor_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ФИО должника (кому был выдан)', 'id': 'debtor_name'}))
    debtor_address = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес должника (по прописке)'}))
    debtor_email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    debtor_phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
'''    court_type = forms.ChoiceField(choices=court_type_list, widget=forms.Select(attrs={'class': 'form-control'}))
    court_type = forms.CharField(widget=forms.Select(attrs={'placeholder': 'Тип суда'}), initial='Тип суда')
    court_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полное наименование судебного участка'}))
    court_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полный адрес судебного участка'}))
    court_order_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер судебного приказа (судебного дела, производства)'}))
    order_issuing_date = forms.DateField(required=True, widget=AdminDateWidget(attrs={'class': 'form-control', 'placeholder': 'Дата вынесения судебного приказа', 'type': 'date', 'onfocus': "this.showPicker && this.showPicker()"}))
    order_receiving_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата получения судебного приказа' ,'type': 'date', 'onfocus': "this.showPicker && this.showPicker()"}))
    collector_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование взыскателя'}))
    collector_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес взыскателя'}))
'''

class CancellationFormPage2(forms.Form):
    court_type = forms.ChoiceField(choices=court_type_list, widget=forms.Select(attrs={'class': 'form-control'}))
    court_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полное наименование судебного участка'}))
    court_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Полный адрес судебного участка'}))
    court_order_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер судебного приказа (судебного дела, производства)'}))
    order_issuing_date = forms.DateField(required=True, widget=AdminDateWidget(attrs={'class': 'form-control', 'placeholder': 'Дата вынесения судебного приказа', 'type': 'date', 'onfocus': "this.showPicker && this.showPicker()"}))
    order_receiving_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата получения судебного приказа' ,'type': 'date', 'onfocus': "this.showPicker && this.showPicker()"}))

class CancellationFormPage3(forms.Form):
    collector_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наименование взыскателя'}))
    collector_address = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес взыскателя'}))