from django.contrib import admin
from django.urls import path
from core.views.base import MainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", MainView.as_view(), name="home"),
]