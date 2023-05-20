from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from rest_framework.permissions import (
    AllowAny,
    DjangoModelPermissions,
    DjangoModelPermissionsOrAnonReadOnly,
    IsAdminUser,
)

from .forms import LessonsForm
from .models import Lesson


def home_view(request):
    context = {}
    context["form"] = LessonsForm()
    return render(request, "lessons/LessonsForm.html", context)


def add_lessons(request):
    if request.method == "POST":
        form = LessonsForm(request.POST)
        if form.is_valid():
            form.save()
            form = LessonsForm()
    else:
        form = LessonsForm()
    return render(request, "lessons/LessonsForm.html", {"form": form})


class LessonListView(ListView):
    login_url = "account_login"
    model = Lesson
    context_object_name = "lessons_list"
    template_name = "lessons/lessons_list.html"
    queryset = Lesson.objects.all()


class LessonDetailView(LoginRequiredMixin, DetailView):
    login_url = "account_login"
    model = Lesson
    context_object_name = "lesson"
    template_name = "lessons/lesson_detail.html"
    queryset = Lesson.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchResultsListView(ListView):
    model = Lesson
    context_object_name = "lessons_list"
    template_name = "lessons/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Lesson.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
