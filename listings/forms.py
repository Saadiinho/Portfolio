from django import forms

class ContactUsForm(forms.Form):
   nom = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))