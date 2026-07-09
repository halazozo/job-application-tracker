from django.db import models
from django.contrib.auth.models import User


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('waiting', 'Waiting'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_link = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    application_date = models.DateField()
    cv_file = models.FileField(upload_to='cvs/', blank=True, null=True)
    cover_letter_file = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"