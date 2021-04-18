from django.forms import forms, CharField, EmailField, Textarea


class ContactForm(forms.Form):

    contact_name = CharField(max_length=31, required=True)
    contact_email = EmailField(max_length=31, required=True)
    subject = CharField(max_length=31)
    content = CharField(required=True, widget=Textarea)
