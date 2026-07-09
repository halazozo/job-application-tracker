from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from .models import JobApplication
from .forms import JobApplicationForm, RegisterForm

def landing(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'applications/landing.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            activation_link = request.build_absolute_uri(
                reverse('activate_account', kwargs={
                    'uidb64': uid,
                    'token': token
                })
            )

            subject = 'Activate your Job Tracker account'
            message = f"""
Hi {user.username},

Thank you for creating an account.

Please click this link to activate your account:

{activation_link}

If you did not create this account, you can ignore this email.
"""

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            messages.success(
                request,
                'Account created. Please check your email to activate your account.'
            )
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)

        messages.success(request, 'Your account has been activated successfully.')
        return redirect('dashboard')

    messages.error(request, 'Activation link is invalid or expired.')
    return redirect('login')
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