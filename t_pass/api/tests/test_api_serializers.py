from rest_framework.request import Request
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from ..models import Stage, Booking, Service
from ..serializers import StageSerializer, BookingSerializer, ServiceSerializer


class StageSerializerTest(TestCase):
    def test_stage_serializer(self):
        service = Service.objects.create(name='Test Service')

        # Valid stage data
        valid_stage_data = {
            'name': 'Test Stage',
            'address': 'Test Address',
            'description': 'Test Description',
            'open_time': timezone.now().time(),
            'close_time': (timezone.now() + timezone.timedelta(hours=2)).time(),
            'services': [service.id]
        }

        serializer = StageSerializer(data=valid_stage_data)
        self.assertTrue(serializer.is_valid())
        stage_instance = serializer.save()

        # Check if the stage is created correctly
        self.assertEqual(stage_instance.name, valid_stage_data['name'])
        self.assertEqual(stage_instance.services.count(), 1)


class BookingSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@email.com')

    def test_booking_serializer_representation(self):
        booking = Booking.objects.create(
            stage=Stage.objects.create(name='Test Stage', address='Test Address', description='Test Description',
                                       open_time=timezone.now().time(),
                                       close_time=(timezone.now() + timezone.timedelta(hours=2)).time()),
            user=self.user,
            start_time=timezone.now().time(),
            finish_time=(timezone.now() + timezone.timedelta(hours=1)).time(),
            date=timezone.now().date(),
            active=True)

        # Check if the serializer correctly represents the booking
        serializer = BookingSerializer(booking)
        representation = serializer.data
        self.assertFalse(representation['active'])
