from django.db import models
from django.contrib.auth import get_user_model
from django_quill.fields import QuillField

User = get_user_model()

# Create your models here.


class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    primary_phone = models.CharField(max_length=15, blank=True, null=True)
    secondary_phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    join_date = models.DateField()
    is_available = models.BooleanField(default=True)
    on_leave = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Committee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    member = models.ManyToManyField(Member)

    def __str__(self):
        return self.title


class MeetingType(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Meeting(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.CASCADE, blank=True, null=True)
    description = QuillField(blank=True, null=True)
    content = QuillField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invited_member = models.ManyToManyField(Member, related_name='invited_member')
    acknowledged_member = models.ManyToManyField(Member, related_name='acknowledged_member')
    attended_member = models.ManyToManyField(Member, related_name='attended_member')

    def __str__(self):
        return self.title
