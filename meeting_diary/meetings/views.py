from django.shortcuts import render, redirect
from django.views import View
from .models import *
from meeting_diary.users.models import *
from .forms import *

# Create your views here.


class HomeView(View):
    def get(self, request):
        departments = Department.objects.filter(user=self.request.user.id).prefetch_related(
            'committee_set').prefetch_related("member_set").prefetch_related("meeting_set").order_by('-created_at')
        add_department_form = DepartmentForm()
        return render(request, 'meetings/home.html', {
            'departments': departments,
            'add_department_form': add_department_form
        })

    def post(self, request):
        add_department_form = DepartmentForm(request.POST)
        if add_department_form.is_valid():
            department = add_department_form.save(commit=False)
            department.user = self.request.user
            department.save()
        return redirect('meetings:home')


class DeleteDepartmentView(View):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        department.delete()
        return redirect('meetings:home')


class UpdateDepartmentView(View):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        update_department_form = DepartmentForm(instance=department)
        return render(request, 'meetings/update_department.html', {
            'department': department,
            'update_department_form': update_department_form
        })

    def post(self, request, pk):
        department = Department.objects.get(pk=pk)
        update_department_form = DepartmentForm(request.POST, instance=department)
        if update_department_form.is_valid():
            update_department_form.save()
        return redirect('meetings:home')


class DepartmentDetailView(View):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        committes = Committee.objects.filter(department=department).prefetch_related("meeting_set")
        add_committee_form = CommitteeForm()
        return render(request, 'meetings/department_detail.html', {
            'department': department,
            "committees": committes,
            'add_committee_form': add_committee_form,
        })

    def post(self, request, pk):
        department = Department.objects.get(pk=pk)
        add_committee_form = CommitteeForm(request.POST)
        if add_committee_form.is_valid():
            committee = add_committee_form.save(commit=False)
            committee.department = department
            committee.save()
        return redirect('meetings:department_detail', pk=department.pk)


class DeleteCommitteeView(View):
    def get(self, request, committee_pk):
        committee = Committee.objects.get(pk=committee_pk)
        pk = committee.department.pk
        committee.delete()
        return redirect('meetings:department_detail', pk=pk)


class UpdateCommitteeView(View):
    def get(self, request, committee_pk):
        committee = Committee.objects.get(pk=committee_pk)
        update_committee_form = CommitteeForm(instance=committee)
        return render(request, 'meetings/update_committee.html', {
            'committee': committee,
            'update_committee_form': update_committee_form
        })

    def post(self, request, committee_pk):
        committee = Committee.objects.get(pk=committee_pk)
        update_committee_form = CommitteeForm(request.POST, instance=committee)
        if update_committee_form.is_valid():
            update_committee_form.save()
        return redirect('meetings:department_detail', pk=committee.department.pk)


class CommitteeDetailView(View):
    def get(self, request, pk):
        committee = Committee.objects.get(pk=pk)
        meetings = Meeting.objects.filter(committee=committee)
        add_member_form = MemberForm()
        add_meeting_form = MeetingForm()
        return render(request, 'meetings/committee_detail.html', {
            'committee': committee,
            'meetings': meetings,
            'add_member_form': add_member_form,
            'add_meeting_form': add_meeting_form
        })

    def post(self, request, pk):
        committee = Committee.objects.get(pk=pk)
        add_member_form = MemberForm(request.POST)
        add_meeting_form = MeetingForm(request.POST)
        if add_member_form.is_valid():
            member = add_member_form.save(commit=False)
            member.committee = committee
            member.save()
        if add_meeting_form.is_valid():
            meeting = add_meeting_form.save(commit=False)
            meeting.committee = committee
            meeting.save()
        return redirect('meetings:committee_detail', pk=committee.pk)
