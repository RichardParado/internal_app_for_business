from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class LeaveType(models.Model):
    name = models.CharField(max_length=50)
    total_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leave_balance = models.ManyToManyField(LeaveType, through='LeaveBalance')

    def __str__(self):
        return self.user.username
    

class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    remaining_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type} - {self.remaining_days} days"
    

class LeaveApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"
    

@receiver(post_save, sender=Employee)
def create_leave_balances_for_new_employee(sender, instance, created, **kwargs):
    if created:
        leave_types = LeaveType.objects.all()
        for leave_type in leave_types:
            LeaveBalance.objects.create(employee=instance, leave_type=leave_type, remaining_days=leave_type.total_days)

@receiver(post_save, sender=LeaveType)
def create_leave_balances_for_new_leave_type(sender, instance, created, **kwargs):
    if created:
        employees = Employee.objects.all()
        for employee in employees:
            LeaveBalance.objects.create(employee=employee, leave_type=instance, remaining_days=instance.total_days)