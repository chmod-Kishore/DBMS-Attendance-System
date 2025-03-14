from django.urls import path
from .views import homepage, student_login, student_register
from .views import teacher_login, teacher_register, student_dashboard,teacher_dashboard  # Import dashboard

urlpatterns = [
    path('', homepage, name='homepage'),
    path('student-login/', student_login, name='student_login'),
    path('teacher-login/', teacher_login, name='teacher_login'),
    path('student-register/', student_register, name='student_register'),
    path('teacher-register/', teacher_register, name='teacher_register'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),  # Add this
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),  # Add this
]
