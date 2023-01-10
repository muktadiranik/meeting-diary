from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import *


app_name = "meetings"
urlpatterns = [
    path("", login_required(HomeView.as_view()), name="home"),
    path("delete-department/<int:pk>/", login_required(DeleteDepartmentView.as_view()), name="delete_department"),
    path("update-department/<int:pk>/", login_required(UpdateDepartmentView.as_view()), name="update_department"),
    path("department-detail/<int:pk>/", login_required(DepartmentDetailView.as_view()), name="department_detail"),
    path("committee-detail/<int:pk>/", login_required(CommitteeDetailView.as_view()), name="committee_detail"),
    path("delete-committee/<int:committee_pk>/", login_required(DeleteCommitteeView.as_view()), name="delete_committee"),
    path("update-committee/<int:committee_pk>/", login_required(UpdateCommitteeView.as_view()), name="update_committee"),
]
