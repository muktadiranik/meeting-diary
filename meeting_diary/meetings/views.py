from django.shortcuts import render
from django.views import View
from .models import *
from meeting_diary.users.models import *

# Create your views here.


class HomeView(View):
    def get(self, request):
        departments = Department.objects.filter(user=self.request.user.id).prefetch_related('committee_set')
        for i in departments:
            for j in i.committee_set.all():
                print(j.title)
        return render(request, 'meetings/home.html', {
            'departments': departments
        })
