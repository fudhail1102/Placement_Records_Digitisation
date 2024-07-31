from django.urls import path 
from .views import RequestPermissionView
urlpatterns = [
    path("actions/ask_permission/", RequestPermissionView.as_view(), name = "request_permission")
]