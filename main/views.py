from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import Course

def index(request):
    output = _('StatusMsg')
    return HttpResponse(output)

def home(request):
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'courses': courses})