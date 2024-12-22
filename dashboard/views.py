from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from leave_tracker.models import LeaveBalance
from .forms import UserProfileForm

# Create your views here.
@login_required
def dashboard(request):
    brands = request.user.brands.all()

    context = {
        'brands': brands
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def profile(request):
    brands = request.user.brands.all()

    try:
        leaves_remaining = LeaveBalance.objects.filter(employee=request.user.employee)
    except:
        leaves_remaining = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)


    context = {
        'brands': brands,
        'leaves_remaining': leaves_remaining,
        'form': form
    }
    return render(request, 'dashboard/profile.html', context)