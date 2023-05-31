# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model  # User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
)

from .decorators import redirect_secretary
from .forms import PurchasePackageForm, CreateAppointmentForm
from .models import Appointment, Instructor, UserProfile, Student, Package
from .serializers import RegisterSerializer
from django.urls import reverse

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class StudentView(ListView):
    model = Appointment
    template_name = "student_view.html"

    def get_queryset(self):
        return Appointment.objects.filter(student__user=self.request.user)


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"


class InstructorListView(ListView):
    template_name = "instructors/instructor_list.html"
    model = Instructor


class InstructorDetailView(DetailView):
    model = Instructor


class PackageListView(ListView):
    model = Package
    template_name = "packages/package_list.html"


class PackageDetailView(DetailView):
    model = Package
    template_name = "packages/package_detail.html"


class AppointmentListView(ListView):
    model = Appointment


class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ["student", "instructor", "date", "location"]


class GeneralScheduleView(ListView):
    model = Appointment
    template_name = "schedule/general_schedule.html"


student_list = StudentListView.as_view()


# student_detail = StudentDetailView.as_view()
def student_detail(request, user_id):
    try:
        user_profile = UserProfile.objects.get(user__id=user_id)
        student = Student.objects.get(user=user_profile)
    except:
        print(f"Student with user_id {user_id} not found!")
        # Handle the exception
        return HttpResponse("Student not found", status=404)

    print(f"Found student: {student}")
    print(student.__dict__)
    appointments = Appointment.objects.filter(student=student)
    context = {"student": student, "appointments": appointments}
    return render(request, "students/student_detail.html", context)


def instructor_detail(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    appointments = Appointment.objects.filter(instructor=user_profile)
    context = {"user_profile": user_profile, "appointments": appointments}
    return render(request, "instructors/instructor_detail.html", context)


instructor_list = InstructorListView.as_view()
# instructor_detail = InstructorDetailView.as_view()
package_list = PackageListView.as_view()
package_detail = PackageDetailView.as_view()
appointment_list = AppointmentListView.as_view()
appointment_detail = AppointmentDetailView.as_view()
appointment_create = AppointmentCreateView.as_view()


def create_appointment(request, user_id):
    # print("Request user_id: ", user_id)
    # print("Request User: ", request.user)
    # print("Request User.id: ", request.user.id)
    # print("Request User.__dict__: ", request.user.__dict__)
    if not request.user.is_authenticated:
        return redirect("login")
    try:
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        student = Student.objects.get(user=user_profile)
        # print("Request UserProfile: ", user_profile)
        # print("Request request.user: ", request.user)
    except UserProfile.DoesNotExist:
        # Handle exception
        pass

    if request.method == "POST":
        form = CreateAppointmentForm(request.POST, user_profile=user_profile)
        if form.is_valid():
            appointment = form.save(commit=False)

            user_profile = UserProfile.objects.get(user_id=request.user.id)
            user_type = user_profile.user_type
            print("user_type", user_type)

            if user_profile.user_type == "Instructor":
                # For instructors, they pick the student
                student_profile = form.cleaned_data["student"]
            elif user_profile.user_type == "Student":
                student_profile = user_profile
            else:
                print(request, "Only students or instructors can create appointments!")
                return redirect("create_appointment")

            duration = form.cleaned_data["duration"]
            student = Student.objects.get(id=form.cleaned_data["student"].id)
            remaining_hours = student.remaining_hours
            if remaining_hours < duration:
                messages.error(
                    request, "The student doesn't have enough hours remaining !"
                )
                return redirect("create_appointment")

            student.remaining_hours -= duration
            print("\n\n")
            print("Request student.remaining_hours : ", student.remaining_hours)
            print("Request duration : ", duration)
            student.save()
            appointment.save()

            messages.success(request, "Appointment successfully created !")
            return redirect("student_detail", user_id=request.user.id)
    else:
        form = CreateAppointmentForm(user_profile=user_profile)

    context = {"form": form}
    return render(request, "appointments/create_appointment.html", context)


def edit_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == "POST":
        form = CreateAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()

            messages.success(request, "Appointment updated !")
            return redirect(reverse("schedule"))
    else:
        form = CreateAppointmentForm(instance=appointment)

    context = {"form": form}
    return render(request, "appointments/edit_appointment.html", context)


def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Appointment deleted !")
        return redirect(reverse("schedule"))

    context = {"appointment": appointment}
    return render(request, "appointments/delete_appointment.html", context)


def purchase_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    student_id = request.user.id
    if request.user.is_authenticated:
        print("\n\n")
        print(request.user.__dict__)
        print("\n\n")
        # return redirect("student_detail", pk=request.user.id)
    else:
        return redirect("login")
    user_profile = UserProfile.objects.get(user__id=student_id)
    student = Student.objects.get(user=user_profile)
    if request.method == "POST":
        form = PurchasePackageForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            total_hours = quantity * package.hours
            student.remaining_hours += total_hours
            student.purchased_hours += total_hours
            student.save()
            for _ in range(quantity):
                student.packages.add(package)
            messages.success(
                request,
                f"You purchased {quantity} x {package.name} package(s). Added {total_hours} hours.",
            )
            print(
                request,
                f"You purchased {quantity} x {package.name} package(s). Added {total_hours} hours.",
            )
            return redirect("student_detail", user_id=request.user.id)
    else:
        form = PurchasePackageForm()
    context = {"form": form, "package": package}
    return render(request, "packages/purchase_package.html", context)


@method_decorator([login_required, redirect_secretary], name="dispatch")
class InstructorScheduleView(ListView):
    model = Appointment
    template_name = "schedule/schedule.html"

    def get_queryset(self):
        try:
            instructor = Instructor.objects.get(user__user=self.request.user)
            return Appointment.objects.filter(instructor=instructor).order_by("date")
        except Instructor.DoesNotExist:
            return Appointment.objects.none()


def get_remaining_hours(request):
    student_id = request.GET.get("student_id")
    try:
        student = Student.objects.get(id=student_id)
        remaining_hours = student.remaining_hours
        return JsonResponse({"remaining_hours": remaining_hours})
    except UserProfile.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)
