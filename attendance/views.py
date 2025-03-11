from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.
def attendance_list(request):
    return render(request,'attendance_list.html');

def homepage(request):
    return render(request,'base.html')

def student_login(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        password = request.POST.get("password")

        user = User.objects.filter(username=userid).first()

        if user:
            user = authenticate(username=userid, password=password)
            if user is not None:
                login(request, user)
                return redirect("student_dashboard")  # Redirect to student dashboard
            else:
                messages.error(request, "Invalid password.")
        else:
            return redirect("student_register")  # Redirect new users to registration

    return render(request, "student_login.html")

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

        # **Here we create the Student object and save it**
        student = Student(
            student_id=student_id,
            dob=dob,
            email=email,
            branch=branch,
            department=department
        )
        student.set_password(password)  # Encrypt password before saving
        student.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("student_login")

    return render(request, "student_register.html")



def teacher_login(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = authenticate(request, username=user_id, password=password)
        
        if user is not None and user.is_staff:  # Ensuring only staff (teachers) can log in
            login(request, user)
            return redirect('teacher_dashboard')  # Redirect to teacher dashboard
        else:
            messages.error(request, "Invalid credentials or not authorized.")
    
    return render(request, "teacher_login.html")


def teacher_register(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('teacher_register')

        if User.objects.filter(username=user_id).exists():
            messages.error(request, "User ID already taken.")
            return redirect('teacher_register')

        # Create a teacher account (staff=True means they are teachers)
        user = User.objects.create_user(username=user_id, password=password)
        user.is_staff = True
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('teacher_login')

    return render(request, "teacher_register.html")

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

        # **Create and save the Teacher object**
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