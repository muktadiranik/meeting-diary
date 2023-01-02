from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['title', 'description']
