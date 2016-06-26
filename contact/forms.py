from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=128, help_text="128 characters max")
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)