from django import forms
from django_quill.forms import QuillFormField
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'description']
