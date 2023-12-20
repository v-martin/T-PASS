from collections import OrderedDict
from django.utils import timezone
from api.models import Stage, Booking
from rest_framework.exceptions import ValidationError


def is_valid_actual(date: timezone.datetime.date, time: timezone.datetime.time) -> bool:
    now = timezone.now()
    booking_datetime = timezone.datetime.combine(date, time)
    booking_datetime = timezone.make_aware(booking_datetime)

    return booking_datetime > now


def _are_overlapping(stage: Stage, date: timezone.datetime.date,
                     start_time: timezone.datetime.time, finish_time: timezone.datetime.time) -> bool:
    overlapping_bookings = Booking.objects.filter(
        stage=stage,
        date=date,
        start_time__lt=finish_time,
        finish_time__gt=start_time,
    )

    return overlapping_bookings.exists()


def _is_not_earlier_or_later(start_time: timezone.datetime.time,
                             finish_time: timezone.datetime.time, stage: Stage) -> bool:
    if start_time < stage.open_time:
        raise ValidationError('Booking start time cannot be earlier than the stage open time.')

    if finish_time > stage.close_time:
        raise ValidationError('Booking finish time cannot be later than the stage close time.')

    return True


def check_constraints(data: dict) -> bool:
    return (_is_not_earlier_or_later(data['start_time'], data['finish_time'], data['stage'])
            and not _are_overlapping(data['stage'], data['date'], data['start_time'], data['finish_time']))

