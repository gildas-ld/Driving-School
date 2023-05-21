from rest_framework.routers import DefaultRouter

from api.views import StudentViewSet, UserProfileViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="students")
router.register(r"user_profile", UserProfileViewSet, basename="user_profile")
# router.register(r"bars", BarViewSet, basename="bar")

urlpatterns = router.urls
