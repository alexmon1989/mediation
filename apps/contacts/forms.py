from django import forms
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact


class ContactForm(forms.Form):
    """Класс формы контактов."""
    contact_name = forms.CharField(max_length=100)
    contact_email = forms.EmailField(max_length=100)
    contact_subject = forms.CharField(max_length=100, required=False)
    contact_message = forms.CharField(max_length=2048)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        html_message = loader.render_to_string(
            'contacts/email/contacts.html',
            {
                'contact_name': self.cleaned_data['contact_name'],
                'contact_email': self.cleaned_data['contact_email'],
                'contact_subject': self.cleaned_data['contact_subject'],
                'contact_message': self.cleaned_data['contact_message'],
            }
        )

        contacts_data = Contact.objects.first()
        recipient_list = [contacts_data.form_email]
        if recipient_list:
            send_mail(
                subject='Повідомлення користувача реєстру медіаторів',
                message='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
                fail_silently=False,
                html_message=html_message
            )
