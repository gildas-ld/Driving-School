# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model  # User = get_user_model()
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
)
from .forms import PurchasePackageForm, CreateAppointmentForm
from .models import Appointment, Instructor, UserProfile
from .models import Student, Package
from .serializers import RegisterSerializer

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


# Provide the view names from urls.py to templates
student_list = StudentListView.as_view()


# student_detail = StudentDetailView.as_view()
def student_detail(request, user_id):
    user_profile = get_object_or_404(UserProfile, user_id=user_id)
    print(user_profile.__dict__)
    appointments = Appointment.objects.filter(student=user_profile)
    context = {"user_profile": user_profile, "appointments": appointments}
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


def create_appointment(request):
    # Vérifier si l'utilisateur est authentifié
    if not request.user.is_authenticated:
        return redirect("login")
    # Vérifier si l'utilisateur est étudiant
    user_profile = UserProfile.objects.get(user=request.user)
    print(user_profile.__dict__)
    # if user_profile.user_type != "STUDENT":
    #     print(request, "Seuls les étudiants peuvent créer des rendez-vous !")
    #     return redirect("student_detail", pk=request.user.id)
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.student = user_profile
            duration = form.cleaned_data["duration"]
            # Vérifier si l'étudiant a suffisamment d'heures
            if user_profile.remaining_hours < duration:
                messages.error(request, "Il ne vous reste plus assez d'heures !")
                return redirect("create_appointment")
            # Déduire la durée du rendez-vous des heures restantes de l'étudiant
            user_profile.remaining_hours -= duration
            user_profile.save()
            appointment.save()
            messages.success(request, "Rendez-vous créé avec succès !")
            print(request, "Rendez-vous créé avec succès !")
            return redirect("student_detail", user_id=request.user.id)
    else:
        form = CreateAppointmentForm()
    context = {"form": form}
    return render(request, "appointments/create_appointment.html", context)


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
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = PurchasePackageForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            total_hours = quantity * package.hours
            user_profile.remaining_hours += total_hours
            user_profile.save()
            student = Student.objects.get(user=user_profile)
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


@method_decorator(login_required, name="dispatch")
class InstructorScheduleView(ListView):
    model = Appointment
    template_name = "schedule/schedule.html"

    def get_queryset(self):
        instructor = Instructor.objects.get(user__user=self.request.user)
        return Appointment.objects.filter(instructor=instructor).order_by("date")
