from django.contrib import admin
from django.urls import path
from core.views.base import MainView
from core.views.taskuser import TaskUserAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainView.as_view(), name="home"),
    path('task-users', TaskUserAPIView.as_view(), name="task-users"),
    path('task-user/<int:id>', TaskUserAPIView.as_view(), name="task-user")
]
