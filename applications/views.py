from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import JobApplication
from .forms import JobApplicationForm


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user).order_by('-created_at')

    query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', '').strip()

    if query:
        applications = applications.filter(
            Q(company_name__icontains=query) |
            Q(job_title__icontains=query) |
            Q(location__icontains=query) |
            Q(notes__icontains=query)
        )

    if status_filter:
        applications = applications.filter(status=status_filter)

    all_applications = JobApplication.objects.filter(user=request.user)

    total = all_applications.count()
    applied = all_applications.filter(status='applied').count()
    waiting = all_applications.filter(status='waiting').count()
    interviews = all_applications.filter(status='interview').count()
    rejected = all_applications.filter(status='rejected').count()
    accepted = all_applications.filter(status='accepted').count()

    def percent(number):
        if total == 0:
            return 0
        return round((number / total) * 100)

    context = {
        'applications': applications,
        'total': total,
        'applied': applied,
        'waiting': waiting,
        'interviews': interviews,
        'rejected': rejected,
        'accepted': accepted,

        'applied_percent': percent(applied),
        'waiting_percent': percent(waiting),
        'interviews_percent': percent(interviews),
        'rejected_percent': percent(rejected),
        'accepted_percent': percent(accepted),

        'query': query,
        'status_filter': status_filter,
    }

    return render(request, 'applications/dashboard.html', context)


@login_required
def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, 'Job application added successfully.')
            return redirect('dashboard')
    else:
        form = JobApplicationForm()

    return render(request, 'applications/add_application.html', {'form': form})


@login_required
def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES, instance=application)

        if form.is_valid():
            form.save()
            messages.success(request, 'Job application updated successfully.')
            return redirect('dashboard')
    else:
        form = JobApplicationForm(instance=application)

    return render(request, 'applications/edit_application.html', {
        'form': form,
        'application': application
    })


@login_required
def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)

    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Job application deleted successfully.')
        return redirect('dashboard')

    return render(request, 'applications/delete_application.html', {'application': application})