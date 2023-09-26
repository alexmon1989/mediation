from django.shortcuts import render
from .models import Page


def index(request):
    return render(
        request,
        template_name='about/index/index.html',
        context={'page': Page.objects.first()}
    )
