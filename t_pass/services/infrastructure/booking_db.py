from django.contrib.auth.models import User
from api.models import Booking
from django.db.models import QuerySet


def create_booking(user: User, data: dict) -> None:
    return Booking.objects.create(user=user, **data)


def get_bookings_by_user(user: User) -> QuerySet:
    return Booking.objects.filter(user=user)


def deactivate_bookings() -> None:
    return Booking.objects.all().update(active=False)
