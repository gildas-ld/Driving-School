from django.urls import path, re_path

from .views import (
    LessonDetailView,
    LessonListView,
    SearchResultsListView,
    home_view,
    add_lessons,
)

# add_lessons
urlpatterns = [
    path("", LessonListView.as_view(), name="lessons_list"),
    re_path("(?P<pk>\d+)/", LessonDetailView.as_view(), name="lesson_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("add_lessons/", add_lessons, name="add_lessons"),
]
