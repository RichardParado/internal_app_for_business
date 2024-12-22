from django.contrib import admin
from .models import LeaveType, LeaveApplication, LeaveBalance, Employee


# Register your models here.
@admin.register(LeaveType)
class LeaveTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_days')
    search_fields = ('name',)

admin.site.register(Employee)


@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'remaining_days')
    search_fields = ('employee',)

@admin.register(LeaveApplication)
class LeaveApplicationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status', 'applied_on')
    search_fields = ('employee', 'leave_type', 'status', 'applied_on')