from django.contrib import admin
from modelap.models import Employee

# Register your models here.
class EmloyeeAdmin(admin.ModelAdmin):
    list_display=['eno', 'ename','esal','eaddr']

admin.site.register(Employee, EmloyeeAdmin)
