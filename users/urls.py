from django.urls import path
from .views import userregister, UserTaskList, AddTask, deletetask
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("register/", userregister, name="user-register"),
    path("home/add/", AddTask.as_view(template_name="users/addnew.html"), name="user-addtask"),
    path("home/delete/", deletetask, name="user-deletetask"),
    path("", UserTaskList.as_view(), name="user-home"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="user-logout")
]