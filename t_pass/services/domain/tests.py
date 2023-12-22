from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.test import APIClient, APITestCase
from api.models import Stage, Booking
from ..domain.schedule import is_valid_actual, _are_overlapping, _is_not_earlier_or_later, check_constraints


class BookingConstraintsTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass', email='test@email.com')

        self.token = Token.objects.create(user=self.user).key

        # Log in the user and get the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_is_valid_actual(self):
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        future_time = timezone.now().time()

        self.assertTrue(is_valid_actual(future_date, future_time))

        past_date = timezone.now().date() - timezone.timedelta(days=1)
        past_time = timezone.now().time()

        self.assertFalse(is_valid_actual(past_date, past_time))

    def test_are_overlapping(self):
        stage = Stage.objects.create(name='Test Stage', open_time=timezone.now().time(), close_time=timezone.now().time())
        date = timezone.now().date()
        start_time = timezone.now().time()
        finish_time = (timezone.now() + timezone.timedelta(hours=2)).time()

        Booking.objects.create(stage=stage, user=self.user, date=date, start_time=start_time, finish_time=finish_time)

        overlapping_start_time = (timezone.now() + timezone.timedelta(hours=1)).time()
        overlapping_finish_time = (timezone.now() + timezone.timedelta(hours=3)).time()

        with self.assertRaises(ValidationError):
            _are_overlapping(stage, date, overlapping_start_time, overlapping_finish_time)

    def test_is_not_earlier_or_later(self):
        stage = Stage.objects.create(name='Test Stage', open_time=timezone.now().time(),
                                     close_time=(timezone.now() + timezone.timedelta(hours=3)).time())
        start_time = (timezone.now() + timezone.timedelta(hours=1)).time()
        finish_time = (timezone.now() + timezone.timedelta(hours=2)).time()

        self.assertTrue(_is_not_earlier_or_later(start_time, finish_time, stage))

        early_start_time = (timezone.now() - timezone.timedelta(hours=1)).time()

        with self.assertRaises(ValidationError):
            _is_not_earlier_or_later(early_start_time, finish_time, stage)

        late_finish_time = (timezone.now() + timezone.timedelta(hours=4)).time()

        with self.assertRaises(ValidationError):
            _is_not_earlier_or_later(start_time, late_finish_time, stage)

    def test_check_constraints(self):
        stage = Stage.objects.create(name='Test Stage', open_time=timezone.now().time(),
                                     close_time=(timezone.now() + timezone.timedelta(hours=3)).time())
        date = timezone.now().date()
        start_time = (timezone.now() + timezone.timedelta(hours=1)).time()
        finish_time = (timezone.now() + timezone.timedelta(hours=2)).time()

        booking_data = {'stage': stage, 'date': date, 'start_time': start_time, 'finish_time': finish_time}

        self.assertTrue(check_constraints(booking_data))

        overlapping_start_time = (timezone.now() + timezone.timedelta(hours=1)).time()
        overlapping_finish_time = (timezone.now() + timezone.timedelta(hours=3)).time()

        Booking.objects.create(stage=stage, user=self.user, date=date,
                               start_time=start_time, finish_time=finish_time)

        with self.assertRaises(ValidationError):
            check_constraints({'stage': stage, 'date': date,
                               'start_time': overlapping_start_time, 'finish_time': overlapping_finish_time})
