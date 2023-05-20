import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all lessons"),
        ]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("lesson_detail", args=[str(self.id)])


class LessonsTaken(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    customuser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    effective = models.BooleanField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    commentary = models.TextField(blank=True, null=True)


class Review(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
