from django.contrib.auth.models import User
from api.models import Booking, Stage, Service
from django.db.models import QuerySet


def create_booking(user: User, data: dict) -> None:
    """
    Create a new booking for the specified user.
    """
    return Booking.objects.create(user=user, **data)


def get_bookings_by_user(user: User) -> QuerySet:
    return Booking.objects.filter(user=user)


def deactivate_bookings() -> None:
    """
    Deactivate all bookings by updating their 'active' status to False.
    """
    return Booking.objects.all().update(active=False)


def get_all_stages() -> QuerySet:
    return Stage.objects.all()


def filter_stages(queryset: QuerySet, params: dict) -> QuerySet:
    """
    Filter stages by a list of service names, name, address, open_time, close_time.
    """
    if 'services' in params:
        queryset = queryset.filter(services__name__in=params['services']).distinct()

    if 'name' in params:
        queryset = queryset.filter(name=params['name'][0]).distinct()

    if 'address' in params:
        queryset = queryset.filter(address=params['address'][0]).distinct()

    if 'open_time' in params:
        queryset = queryset.filter(open_time=params['open_time'][0]).distinct()

    if 'close_time' in params:
        queryset = queryset.filter(close_time=params['close_time'][0]).distinct()

    return queryset


def get_all_services() -> QuerySet:
    return Service.objects.all()
