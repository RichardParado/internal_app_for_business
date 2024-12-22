from django import forms
from .models import LeaveApplication, LeaveBalance

class LeaveApplicationForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ['leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'leave_type': forms.Select(attrs={'class': 'form-control mb-2'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'reason': forms.TextInput(attrs={'class': 'form-control mb-2'})

        }

    def clean(self):
        cleaned_data = super().clean()
        leave_type = cleaned_data.get('leave_type')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        employee = self.instance.employee

        if leave_type and start_date and end_date:
            leave_days = (end_date - start_date).days + 1
            if leave_days > 0:
                # Check if the employee has enough remaining days
                leave_balance = LeaveBalance.objects.get(employee=employee, leave_type=leave_type)
                if leave_balance.remaining_days < leave_days:
                    raise forms.ValidationError(
                        f"Not enough remaining leave days for {leave_type.name}. You have {leave_balance.remaining_days} days left."
                    )
            else:
                raise forms.ValidationError(
                    "Please check the Start Date and End Date again."
                )
        return cleaned_data