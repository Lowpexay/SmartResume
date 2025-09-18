from django import forms

class ResumeForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    summary = forms.CharField(label='Resumo', widget=forms.Textarea)
