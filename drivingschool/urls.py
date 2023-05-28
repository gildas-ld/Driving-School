from django.urls import include, path
from drivingschool.views import (
    create_appointment,
    delete_appointment,
    edit_appointment,
    get_remaining_hours,
    instructor_detail,
    instructor_list,
    InstructorScheduleView,
    package_detail,
    package_list,
    purchase_package,
    student_detail,
    student_list,
)

drivingschool_apis = [
    path("", include("api.urls")),
]
appointments_urls = [
    path(
        "delete_appointment/<int:appointment_id>/",
        delete_appointment,
        name="delete_appointment",
    ),
    path(
        "edit_appointment/<int:appointment_id>/",
        edit_appointment,
        name="edit_appointment",
    ),
    path("create_appointment/", create_appointment, name="create_appointment"),
    path("schedule/", InstructorScheduleView.as_view(), name="schedule"),
    path("get_remaining_hours/", get_remaining_hours, name="get_remaining_hours"),
]
packages_urls = [
    path("packages/", package_list, name="package_list"),
    path("packages/<int:pk>/", package_detail, name="package_detail"),
    path("packages/<int:pk>/purchase/", purchase_package, name="purchase_package"),
]
drivingschool_urlpatterns = [
    path("students/", student_list, name="student_list"),
    path("students/<int:user_id>/", student_detail, name="student_detail"),
    path("instructors/", instructor_list, name="instructor_list"),
    path("instructors/<int:pk>/", instructor_detail, name="instructor_detail"),
    path("purchase_package/", purchase_package, name="purchase_package"),
    path("api/", include(drivingschool_apis)),
    path("", include(appointments_urls)),
    path("", include(packages_urls)),
]
