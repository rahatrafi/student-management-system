from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='student_create'),
    path('edit/<int:id>/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:id>/', StudentDeleteView.as_view(), name='student_delete'),
]
