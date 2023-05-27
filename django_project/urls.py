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
from drivingschool.urls import drivingschool_urlpatterns
from drivingschool.views import RegisterView

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
