from django.contrib import admin
from schoolapp.models import Student

# Register your models here.
class schoolAdmin(admin.ModelAdmin):
    list_display=['Name', 'Father_Name', 'Mother_Name', 'Age', 'Address', 'Class_For_Admission']

admin.site.register(Student, schoolAdmin)
