from django.contrib import admin
from .models import Level, Exam, Section

@admin.register(Level)
class levelPanel (admin.ModelAdmin) :
    list_display = ['name','id']


@admin.register(Exam)
class examPanel (admin.ModelAdmin) :
    list_display = ['name','level','from_section','to_section','id']


@admin.register(Section)
class sectionPanel (admin.ModelAdmin) :
    list_display = ['number','exam','level','state','id']
