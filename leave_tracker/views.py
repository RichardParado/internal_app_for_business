from django.shortcuts import render, redirect, get_object_or_404
from .forms import LeaveApplicationForm
from .models import LeaveApplication, LeaveBalance
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
@login_required
def leave_list(request):
    brands = request.user.brands.all()

    if request.user.is_superuser:
        leave_applications = LeaveApplication.objects.all().order_by('-applied_on')
    else:
        leave_applications = LeaveApplication.objects.filter(employee=request.user.employee).all().order_by('-applied_on')

    context = {
        'brands': brands,
        'leave_applications': leave_applications
    }
    return render(request, 'leave_tracker/leave-list.html', context)

@login_required
def leave_detail(request, application_id):
    brands = request.user.brands.all()

    if request.user.is_superuser:
        leave_application = LeaveApplication.objects.get(id=application_id)
    else:
        leave_application = get_object_or_404(LeaveApplication, employee=request.user.employee, id=application_id)

    context = {
        'brands': brands,
        'leave_application': leave_application
    }
    return render(request, 'leave_tracker/leave-detail.html', context)

@login_required
def apply_leave(request):
    brands = request.user.brands.all()

    if request.method == 'POST':
        form = LeaveApplicationForm(request.POST)
        form.instance.employee = request.user.employee

        if form.is_valid():
            leave_application = form.save(commit=False)
            
            # Ensure LeaveBalance exists
            leave_balance, created = LeaveBalance.objects.get_or_create(
                employee=leave_application.employee,
                leave_type=leave_application.leave_type,
                defaults={'remaining_days': leave_application.leave_type.total_days}
            )

            leave_application.save()
            send_mail(
                subject=f'Leave application - {leave_application.employee}',
                message=f'A new leave application has been submitted by {leave_application.employee}.\nLeave Type: {leave_application.leave_type}\nReason: {leave_application.reason}\nStart Date: {leave_application.start_date}\nEnd Date: {leave_application.end_date}',
                from_email='richard@analyticsstation.com',
                recipient_list=['richard.parado2908@gmail.com']
            )
            messages.success(request, 'Leave Applied Successfully')
            return redirect('leave-list')
        else:
            messages.error(request, 'Error Applying Leave')

        
    else:
        form = LeaveApplicationForm()

    context = {
        'brands': brands,
        'form': form
    }
    return render(request, 'leave_tracker/apply-leave.html', context)

@login_required
def approve_leave(request, application_id):
    if request.user.is_staff:
        application = LeaveApplication.objects.get(id=application_id)

        if application.processed:
            return redirect('leave-list')
        
        application.status = 'Approved'
        application.processed = True
        application.save()
        
        # Reduce the leave balance
        leave_balance = LeaveBalance.objects.get(employee=application.employee, leave_type=application.leave_type)
        leave_days = (application.end_date - application.start_date).days + 1
        leave_balance.remaining_days -= leave_days
        leave_balance.save()
        messages.success(request, 'Leave Approved Successfully')
        
        return redirect('leave-list')
    else:
        messages.warning(request, 'Error Approving Leave')
        return redirect('leave-list')


@login_required 
def reject_leave(request, application_id):
    if request.user.is_staff:
        application = LeaveApplication.objects.get(id=application_id)

        if application.processed:
            return redirect('leave-list')
        
        application.status = 'Rejected'
        application.processed = True
        application.save()
        messages.success(request, 'Leave Rejected Successfully')
        
        return redirect('leave-list')
    else:
        messages.warning(request, 'Error Rejecting Leave')
        return redirect('leave-list')

