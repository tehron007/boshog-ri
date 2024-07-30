from django.shortcuts import render
from .models import Index


def index(request):
    a = Index.objects.all()

    context = {
        'index': a
    }
    return render(request, 'index.html', context)
