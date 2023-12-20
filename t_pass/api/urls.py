from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StageViewSet, BookingViewSet, DeactivateAllBookingsView


router = DefaultRouter()
router.register(r'stages', StageViewSet, 'stages')
router.register(r'bookings', BookingViewSet, 'bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('deactivate-bookings/', DeactivateAllBookingsView.as_view(), name='deactivate-bookings')
]
