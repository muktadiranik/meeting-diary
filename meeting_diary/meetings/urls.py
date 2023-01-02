from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import *


app_name = "meetings"
urlpatterns = [
    path("", login_required(HomeView.as_view()), name="home"),
    path("delete-department/<int:pk>/", login_required(DeleteDepartmentView.as_view()), name="delete_department"),
    path("update-department/<int:pk>/", login_required(UpdateDepartmentView.as_view()), name="update_department"),
]
