from datetime import date

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ValidationError

from .models import Appointment, Instructor, Student, UserProfile


class PurchasePackageForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "student",
            "instructor",
            "date",
            "duration",
            "lesson_type",
            "location",
        ]
        labels = {
            "student": "Étudiant",
            "instructor": "Instructeur",
            "date": "Date",
            "duration": "Durée (en heures) de la leçon",
            "lesson_type": "Type de leçon",
            "location": "Emplacement",
        }

        widgets = {
            "duration": forms.TextInput(
                attrs={
                    "type": "number",
                    "class": "form-control form-control-sm",
                    "min": "1",
                    "max": "20",
                }
            ),
            "instructor": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateTimeInput(
                format=("%Y-%m-%dT%H:%M"),
                attrs={
                    "type": "datetime-local",
                    "class": "form-control form-control-sm",
                    "placeholder": "Sélectionnez une date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        user_profile = kwargs.pop("user_profile", None)
        print("\n🚀 > file : drivingschool/forms.py:72 > user_profile:", user_profile)

        instance = kwargs.get("instance", None)
        print("\n🚀 > file : drivingschool/forms.py:75 > instance:", instance)

        super().__init__(*args, **kwargs)
        today = date.today().strftime("%Y-%m-%dT%H:%M")
        self.fields["date"].widget.attrs["min"] = today

        self.fields["instructor"].queryset = Instructor.objects.all()
        if instance:
            self.fields["date"].initial = instance.date.strftime("%Y-%m-%dT%H:%M")

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control form-control-sm"

        else:
            self.fields["date"].widget.attrs["min"] = today
            self.fields["date"].initial = today

        if user_profile:
            if user_profile.user_type == "Instructor":
                self.fields["instructor"].initial = user_profile
                self.fields["instructor"].queryset = Instructor.objects.filter(
                    user=user_profile
                )
                self.fields["instructor"].disabled = True
            elif user_profile.user_type == "Student":
                try:
                    student_instance = Student.objects.get(user=user_profile)
                    self.fields["student"].initial = student_instance
                    self.fields["student"].queryset = Student.objects.filter(
                        user=user_profile
                    )
                    # self.fields["student"].disabled = True
                except Student.DoesNotExist:
                    pass

            try:
                instructor_instance = Instructor.objects.get(user=user_profile)
                self.fields["instructor"].initial = instructor_instance
                self.fields["student"].queryset = Student.objects.all()
            except Instructor.DoesNotExist:
                pass

    def clean_duration(self):
        duration = self.cleaned_data["duration"]
        student = Student.objects.get(user_id=self.cleaned_data["student"].user_id)
        if student:
            if student.remaining_hours < duration:
                raise ValidationError("Il ne vous reste plus assez d'heures !")
        return duration
