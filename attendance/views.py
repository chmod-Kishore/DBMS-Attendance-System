from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Teacher
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



# Homepage
def homepage(request):
    return render(request, 'base.html')

def student_register(request):
    if request.method == "POST":
        student_id = request.POST.get("student-id")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        branch = request.POST.get("branch")
        department = request.POST.get("department")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("student_register")

        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already registered!")
            return redirect("student_register")

        # Create Student (It already extends User, so no need for a separate User object)
        student = Student.objects.create_user(
            username=student_id,
            student_id=student_id,
            dob=dob,
            email=email,
            branch=branch,
            department=department,
            password=password
        )
        student.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("student_login")

    return render(request, "student_register.html")


# Student Login
@csrf_exempt 

def student_login(request):
    if request.method == "POST":
        student_id = request.POST.get("user_id")  # Ensure the correct field is used
        print(f"Student id is: {student_id}")
        password = request.POST.get("password")
        print(f"Password is: {password}")
        user = authenticate(student_id=student_id, password=password)  # Authenticate correctly
        

        print(f"DEBUG: Authenticated User: {user}")  # Debugging

        if user is not None:
            login(request, user)
            return redirect("student_dashboard")  # Redirect to dashboard
        else:
            print("DEBUG: Login failed.")  # Debugging
            return render(request, "student_login.html", {"error": "Invalid credentials"})

    return render(request, "student_login.html")

# Student Dashboard
@login_required
def student_dashboard(request):
    return render(request, "student_dashboard.html")

# Teacher Registration
def teacher_register(request):
    if request.method == "POST":
        teacher_id = request.POST.get("teacher-id")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        department = request.POST.get("department")
        specialization = request.POST.get("specialization")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("teacher_register")

        if Teacher.objects.filter(teacher_id=teacher_id).exists():
            messages.error(request, "Teacher ID already registered!")
            return redirect("teacher_register")

        # Create and save Teacher object
        teacher = Teacher(
            teacher_id=teacher_id,
            dob=dob,
            email=email,
            department=department,
            specialization=specialization
        )
        teacher.set_password(password)  # Encrypt password before saving
        teacher.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("teacher_login")

    return render(request, "teacher_register.html")

# Teacher Login
def teacher_login(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        user = authenticate(request, username=user_id, password=password)

        if user is not None and user.is_staff:  # Ensuring only teachers can log in
            auth_login(request, user)
            return redirect("teacher_dashboard")  # Redirect to teacher dashboard
        else:
            messages.error(request, "Invalid credentials or not authorized.")
            return redirect("teacher_login")

    return render(request, "teacher_login.html")

# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    return render(request, "teacher_dashboard.html")

# QR Code Generation (Placeholder)
@login_required
def generate_qr(request):
    if request.method == "POST":
        class_id = request.POST.get("class_id")
        # QR Code generation logic will be added later
        messages.success(request, f"QR Code generated for class {class_id}.")
        return redirect("teacher_dashboard")

    return render(request, "generate_qr.html")

def dashboard(request):
    return render(request, "dashboard.html")

def attendance_list(request):
    return render(request, "attendance_list.html")
