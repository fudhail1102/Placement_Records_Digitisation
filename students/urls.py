from django.urls import path 
from .views import (
    BatchListView,
    DepartmentList,
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    CompanyListView,
    CompanyDetailView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
    PlacementActivityListView,
    PlacementActivityDetailView,
    PlacementActivityCreateView,
    PlacementActivityUpdateView,
    PlacementActivityDeleteView,
    HomeView
)
urlpatterns = [
    path("", HomeView.as_view(), name = 'home'),
    path("students/", BatchListView.as_view(), name="batch_list"),
    path("students/<int:batch>/",DepartmentList.as_view(),name="department_list"),
    path("students/<int:batch>/<str:branch>/",StudentListView.as_view(), name = "student_list" ),
    path("student/<int:register_no>/", StudentDetailView.as_view(), name = "student_detail"),
    path("student/create/",StudentCreateView.as_view(), name = "student_create"),
    path("student/<int:register_no>/update/", StudentUpdateView.as_view(), name = "student_update"),
    path("student/<int:register_no>/delete/", StudentDeleteView.as_view(), name = "student_delete"),

    path("company/", CompanyListView.as_view(), name = "company_list"),
    path("company/create/", CompanyCreateView.as_view(), name = "company_create"),
    path("company/<str:company>/", CompanyDetailView.as_view(), name = "company_detail"),
    path("company/<int:pk>/update/", CompanyUpdateView.as_view(), name = "company_update"),
    path("company/<int:pk>/delete/", CompanyDeleteView.as_view(), name = "company_delete"),

    path("student/<int:digital_id>/placement/", PlacementActivityListView.as_view(), name = "placement_list"),
    path("student/<int:digital_id>/placement/create/", PlacementActivityCreateView.as_view(), name = "placement_create"),
    path("student/<int:digital_id>/placement/<int:pk>/", PlacementActivityDetailView.as_view(), name = "placement_detail"),
    path("student/<int:digital_id>/placement/<int:pk>/update/", PlacementActivityUpdateView.as_view(), name = "placement_update"),
    path("student/<int:digital_id>/placement/<int:pk>/delete/", PlacementActivityDeleteView.as_view(), name = "placement_delete"),


]