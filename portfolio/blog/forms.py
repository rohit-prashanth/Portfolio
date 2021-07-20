from django import forms

class user_contact_form(forms.Form):
    name = forms.CharField(help_text='should be less than 10 characters')
    email = forms.EmailField(initial='example@gmail.com')
    additionaldetails = forms.CharField(widget=forms.Textarea)
