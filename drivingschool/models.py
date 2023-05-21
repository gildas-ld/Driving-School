from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ("STUDENT", "Student"),
        ("INSTRUCTOR", "Instructor"),
        ("SECRETARY", "Secretary"),
        ("ADMIN", "Admin"),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    remaining_hours = models.PositiveIntegerField(default=0)


class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    packages = models.ManyToManyField("Package")


class Instructor(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"

    # def __str__(self):
    #     return self.user.user.username
    def full_name(self):
        return f"{self.user.user.first_name} {self.user.user.last_name}"


class Package(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hours = models.IntegerField()
    cover = models.TextField()


class Appointment(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.PositiveIntegerField(help_text="Durée de la leçon", default=0)
    lesson_type = models.CharField(
        max_length=100,
        choices=[
            ("autoroute", "Autoroute"),
            ("parking", "Parking"),
            ("ville", "Conduite en ville"),
        ],
        default="ville",
    )
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Lesson on {self.date} with {self.student} and {self.instructor}"

    class Meta:
        ordering = ["-date"]
