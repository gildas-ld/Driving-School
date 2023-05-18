from rest_framework.routers import DefaultRouter

from drivingschool.views import BarViewSet, OrderViewSet, ReferenceViewSet, StockViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"references", ReferenceViewSet, basename="reference")
router.register(r"bars", BarViewSet, basename="bar")
router.register(r"stocks", StockViewSet, basename="stock")
router.register(r"orders", OrderViewSet, basename="orders")
urlpatterns = router.urls
