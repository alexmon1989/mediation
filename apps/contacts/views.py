from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import Contact
from .forms import ContactForm


def index(request):
    """Відображає сторінку зворотнього зв'язку."""
    return render(
        request,
        template_name='contacts/index/index.html',
        context={'contacts_data': Contact.objects.first()}
    )


@require_POST
def send_email(request):
    """Відправляє E-Mail з даними форми зворотнього зв'язку."""
    if request.POST.get('norobot') != '':
        message = '{:err:unexpected:}'
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.send_email()
            except Exception as error:
                message = '{:err:unexpected:}'
            else:
                message = '{:success:}'
        else:
            message = '{:err:required:}'
    return HttpResponse(message)
