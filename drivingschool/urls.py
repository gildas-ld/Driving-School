from django.urls import include, path
from drivingschool.views import (
    student_list,
    student_detail,
    instructor_list,
    package_list,
    package_detail,
    purchase_package,
    instructor_detail,
    create_appointment,
    InstructorScheduleView,
)

drivingschool_apis = [
    path("", include("api.urls")),
]
drivingschool_urlpatterns = [
    path("students/", student_list, name="student_list"),
    path("schedule/", InstructorScheduleView.as_view(), name="schedule"),
    path("students/<int:user_id>/", student_detail, name="student_detail"),
    path("instructors/", instructor_list, name="instructor_list"),
    path("instructors/<int:pk>/", instructor_detail, name="instructor_detail"),
    path("packages/", package_list, name="package_list"),
    path("packages/<int:pk>/", package_detail, name="package_detail"),
    path("create_appointment/", create_appointment, name="create_appointment"),
    path("packages/<int:pk>/purchase/", purchase_package, name="purchase_package"),
    path("purchase_package/", purchase_package, name="purchase_package"),
    path("api/", include(drivingschool_apis)),
]
