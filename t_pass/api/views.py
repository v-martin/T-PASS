from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stage, Booking
from .serializers import StageSerializer, BookingSerializer, ServiceSerializer

from services.infrastructure import api_db


class StageViewSet(viewsets.ModelViewSet):
    """
    View for managing musical stages.
    - CRUD operations on stages.
    - Supports filtering by services.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StageSerializer

    # Retrieve the list of stages. Supports filtering by services using query parameters.
    def get_queryset(self):
        queryset = api_db.get_all_stages()
        params = dict(self.request.query_params)

        if params:
            queryset = api_db.filter_stages(queryset, params)

        return queryset


class ServiceViewSet(viewsets.ModelViewSet):
    """
    View for managing services.
    - CRUD operations on services.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return api_db.get_all_services()


class BookingViewSet(viewsets.ModelViewSet):
    """
    View for managing bookings.
    - CRUD operations on bookings.
    - Supports user-specific bookings creation.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        return api_db.get_bookings_by_user(self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeactivateAllBookingsView(APIView):
    """
    View for deactivating all bookings.
    - Admin-only endpoint.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BookingSerializer

    def patch(self, request):
        api_db.deactivate_bookings()
        return Response({'detail': 'All bookings deactivated successfully.'}, status=status.HTTP_200_OK)
