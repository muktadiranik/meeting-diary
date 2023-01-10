from django import forms
from django_quill.forms import QuillFormField
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'description']


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ['title', 'description']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'primary_phone',
                  'secondary_phone', 'email', 'address', 'designation',
                  'join_date', 'is_available', 'on_leave']


class MeetingTypeForm(forms.ModelForm):
    class Meta:
        model = MeetingType
        fields = ['title', 'description']


class MeetingForm(forms.ModelForm):
    content = QuillFormField()

    class Meta:
        model = Meeting
        fields = ['title', 'description', 'meeting_type', 'start_time',
                  'end_time', 'committee', 'invited_member', 'content']
