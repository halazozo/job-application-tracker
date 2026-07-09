from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company_name',
            'job_title',
            'job_link',
            'location',
            'status',
            'application_date',
            'cv_file',
            'cover_letter_file',
            'notes',
        ]

        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Amazon'
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Delivery Driver'
            }),
            'job_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/job-post'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Braunschweig'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'application_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'cv_file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'cover_letter_file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Example: Applied online, waiting for reply...'
            }),
        }