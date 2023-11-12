from django.contrib import admin

# Register your models here.

from .models import Student, Section, Year, Branch

admin.site.register(Student)
admin.site.register(Section)
admin.site.register(Year)
admin.site.register(Branch)
