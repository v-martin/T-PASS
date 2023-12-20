from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stage, Booking
from .serializers import StageSerializer, BookingSerializer
from services.infrastructure.booking_db import get_bookings_by_user, deactivate_bookings


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer


class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        return get_bookings_by_user(self.request.user)


class DeactivateAllBookingsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def patch(self, request):
        deactivate_bookings()
        return Response({'detail': 'All bookings deactivated successfully.'}, status=status.HTTP_200_OK)
