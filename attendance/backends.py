from django.contrib.auth.backends import ModelBackend
from attendance.models import Student

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Student.objects.get(student_id=username)  # Match USERNAME_FIELD
            if user.check_password(password):
                return user
        except Student.DoesNotExist:
            return None
