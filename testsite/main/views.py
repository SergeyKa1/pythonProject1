from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'text': 'text',
    }
    return render(request, template_name='main/index.html', context=context)

