from django.contrib import admin
from coursera.models import Group, Student

class ChoiceInline(admin.TabularInline):
    model = Student

class GroupAdmin(admin.ModelAdmin):
    fields = ['group_text']
    inlines = [ChoiceInline]

admin.site.register(Group, GroupAdmin)

