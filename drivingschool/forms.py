from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Appointment, Instructor, UserProfile
from datetime import date


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
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

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
            "duration": "Durée",
            "lesson_type": "Type de leçon",
            "location": "Emplacement",
        }

    def __init__(self, *args, **kwargs):
        instructor_user = kwargs.pop("instructor_user", None)
        super().__init__(*args, **kwargs)
        today = date.today().strftime("%Y-%m-%d")
        self.fields["date"].widget.attrs["min"] = today

        self.fields["instructor"].queryset = Instructor.objects.all()
        self.fields["student"].queryset = UserProfile.objects.filter(
            user_type="Student"
        )
        if instructor_user:
            instructor_instance = Instructor.objects.get(user__user=instructor_user)
            self.fields["instructor"].initial = instructor_instance

    def clean_duration(self):
        duration = self.cleaned_data["duration"]
        student = self.cleaned_data.get("student", None)
        if student:
            if student.remaining_hours < duration:
                raise ValidationError("Il ne vous reste plus assez d'heures !")
        return duration
