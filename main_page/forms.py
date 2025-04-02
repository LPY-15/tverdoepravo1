from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    phone = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    comment = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}))