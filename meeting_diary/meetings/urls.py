from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import *


app_name = "meetings"
urlpatterns = [
    path("", login_required(HomeView.as_view()), name="home"),
]
