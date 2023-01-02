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
