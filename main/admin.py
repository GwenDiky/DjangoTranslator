from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Course
# Register your models here.

admin.site.register(Course, TranslatableAdmin)