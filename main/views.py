from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    output = _('StatusMsg')
    return HttpResponse(output)

def home(request):
    return render(request, 'main/index.html', {})