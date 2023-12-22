from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Stage, Booking
from ..serializers import StageSerializer, BookingSerializer


class BookingViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='tests@email.com')

        self.stage_data = {'name': 'Test Stage', 'address': 'Test Address', 'description': 'Test Description',
                           'open_time': '10:00', 'close_time': '23:00'}
        self.stage = Stage.objects.create(**self.stage_data)

        self.booking_data = {
            'stage': self.stage.id,
            'user': self.user.id,
            'start_time': '12:00',
            'finish_time': '14:00',
            'date': '2024-01-01',
            'active': True
        }

    def test_create_booking_valid(self):
        self.client.force_authenticate(user=self.user)

        # Ensure the number of bookings increases by 1 after creating a new booking
        response = self.client.post('/api/bookings/', data=self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

    def test_create_booking_invalid(self):
        # Invalid booking
        self.booking_data = {
            'stage': self.stage.id,
            'user': self.user.id,
            'start_time': '12:00',
            'finish_time': '14:00',
            'date': '2022-01-01',
            'active': True
        }

        self.client.force_authenticate(user=self.user)

        # Ensure the booking was not created
        response = self.client.post('/api/bookings/', data=self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Booking.objects.count(), 0)

    def test_create_booking_unauthenticated(self):
        # Ensure an unauthenticated user cannot create a booking
        response = self.client.post('/api/bookings/', data=self.booking_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_bookings(self):
        self.client.force_authenticate(user=self.user)

        self.booking_data['stage'] = Stage.objects.get(pk=self.booking_data['stage'])
        self.booking_data['user'] = User.objects.get(pk=self.booking_data['user'])
        booking = Booking.objects.create(**self.booking_data)

        # Ensure the user can retrieve their bookings
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], booking.id)

    def test_deactivate_all_bookings_admin(self):
        # Create an admin user
        admin_user = User.objects.create_user(username='adminuser', password='adminpassword', is_staff=True)

        self.client.force_authenticate(user=admin_user)

        self.booking_data['stage'] = Stage.objects.get(pk=self.booking_data['stage'])
        self.booking_data['user'] = User.objects.get(pk=self.booking_data['user'])
        booking = Booking.objects.create(**self.booking_data)

        # Ensure all bookings are deactivated
        response = self.client.patch('/api/deactivate-bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Booking.objects.get(id=booking.id).active)
