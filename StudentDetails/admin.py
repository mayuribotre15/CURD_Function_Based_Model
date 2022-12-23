from django.contrib import admin
from .models import StudentDetails

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'l_name', 'email', 'mobile_no']

admin.site.register(StudentDetails, StudentAdmin)