from collections import OrderedDict
from django.utils import timezone
from api.models import Booking


def is_valid_actual(date: timezone.datetime.date, time: timezone.datetime.time) -> bool:
    now = timezone.now()
    booking_datetime = timezone.datetime.combine(date, time)
    booking_datetime = timezone.make_aware(booking_datetime)

    return booking_datetime > now


def are_overlapping(stage, date, start_time, finish_time) -> bool:
    overlapping_bookings = Booking.objects.filter(
        stage=stage,
        date=date,
        start_time__lt=finish_time,
        finish_time__gt=start_time,
    )

    return overlapping_bookings.exists()

