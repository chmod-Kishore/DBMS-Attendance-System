from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):  # Inherits Django's user system
    teacher_id = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    USERNAME_FIELD = "teacher_id"  # Login using teacher ID
    REQUIRED_FIELDS = ["dob", "email", "department", "specialization"]
    
    def __str__(self):
        return f"{self.teacher_id} - {self.email}"

class Student(AbstractUser):  # Inherits Django's user system
    student_id = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    USERNAME_FIELD = "student_id"  # Login using student ID
    REQUIRED_FIELDS = ["dob", "email", "branch", "department"]
    
    def __str__(self):
        return f"{self.student_id} - {self.email}"