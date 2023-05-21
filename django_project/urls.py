from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from drivingschool.views import (
    RegisterView,
    student_list,
    student_detail,
    instructor_list,
    package_list,
    package_detail,
    purchase_package,
    instructor_detail,
    create_appointment,
)

API_TITLE = "Driving School"
API_DESCRIPTION = "Driving School's API"
schema_view = get_schema_view(title=API_TITLE)
api_urlpatterns = [
    path(
        "", include("api.urls")
    ),  # re_path(r"statistics", StatisticsView.as_view(), name="statistics"),
    # Auth/Token :
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
]
drivingschool_apis = [
    path("", include("api.urls")),
]
drivingschool_urlpatterns = [
    path("students/", student_list, name="student_list"),
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
urlpatterns = [  # User management
    path("accounts/", include("allauth.urls")),  # Local apps
    path("", include("pages.urls")),
    # re_path(r"^home/", HomePageView.as_view(), name="home"),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api/", include(api_urlpatterns)),
    re_path(r"^ds/", include(drivingschool_urlpatterns)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    re_path(
        r"^api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    re_path(
        r"^api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
