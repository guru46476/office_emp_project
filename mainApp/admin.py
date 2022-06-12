from django.contrib import admin
# Register your models here.
from .models import Employee

# YOU CAN REGISTER DATABASE TABLE WITH 2 OPTIONS, LISTED BELOW.

# option 1: --------->
# admin.site.register((
#     Employee,
# ))
# ---------------------------------------------------------------------------------------------------------
# option 2: ------>[Best]
# -----------------for table viewing in admin pannel---------------------->
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','role','salary','email','phone','location','hiredate']