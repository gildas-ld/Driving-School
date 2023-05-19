from django.urls import include, path, re_path

from .views import HomePageView, AboutPageView, LessonsPageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("lessons/", LessonsPageView.as_view(), name="lessons"),
    path("", HomePageView.as_view(), name="home"),
]
