from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='To')
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
