from django import forms
from .models import JobApplication
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobApplication
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Choose a password'
        }),
        help_text=''
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repeat your password'
        }),
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already used.')

        return email
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