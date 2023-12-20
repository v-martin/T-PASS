from django.db import models
from django.contrib.auth.models import User


class Stage(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stage'


class Booking(models.Model):
    stage = models.ForeignKey(to=Stage, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s booking by %s' % (self.stage, self.user.name)

    class Meta:
        db_table = 'booking'
        ordering = ['date', 'start_time', 'active']

