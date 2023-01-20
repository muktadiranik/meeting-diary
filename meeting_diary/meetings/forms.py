from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        exclude = ["user"]


class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = "__all__"
        exclude = ["department"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommitteeForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = Member.objects.filter(
            department=self.initial["department"])


class MemberForm(forms.ModelForm):
    join_date = forms.fields.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'}), required=False)

    class Meta:
        model = Member
        fields = "__all__"
        exclude = ["department"]


class MeetingTypeForm(forms.ModelForm):
    class Meta:
        model = MeetingType
        fields = "__all__"
        exclude = ["department"]


class MeetingForm(forms.ModelForm):
    start_time = forms.fields.DateTimeField(widget=forms.widgets.DateTimeInput(
        attrs={'type': 'datetime-local'}), required=False)
    end_time = forms.fields.DateTimeField(widget=forms.widgets.DateTimeInput(
        attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = Meeting
        fields = "__all__"
        exclude = ["department", "committee", "acknowledged_member", "attended_member", "content_document"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.fields['invited_member'].queryset = Member.objects.filter(
            id__in=self.initial["committee"].member.all())
        self.fields["meeting_type"].queryset = MeetingType.objects.filter(
            department=self.initial["committee"].department)
