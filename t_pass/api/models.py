from django.db import models
from django.contrib.auth.models import User
from django.db.models import CheckConstraint, Q, F


class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'service'


class Stage(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    services = models.ManyToManyField(to=Service, related_name='services', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stage'
        constraints = [
            CheckConstraint(
                check=Q(open_time__lt=F('close_time')),
                name='open_time_earlier_than_close_time'
            ),
        ]


class Booking(models.Model):
    stage = models.ForeignKey(to=Stage, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s booking by %s' % (self.stage, self.user.name)

    class Meta:
        db_table = 'booking'
        ordering = ['date', 'start_time', 'active']

