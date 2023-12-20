from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Stage, Booking
from services.infrastructure.booking_db import create_booking
from services.domain.schedule import is_valid_actual, are_overlapping


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.stage = validated_data.get('stage', instance.stage)
        instance.date = validated_data.get('date', instance.date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.finish_time = validated_data.get('finish_time', instance.finish_time)
        instance.active = validated_data.get('active', instance.active)

        if not is_valid_actual(instance.date, instance.start_time):
            raise ValidationError('Stages can not be booked on the past time.')

        if instance.active and are_overlapping(instance.stage, instance.date,
                                               instance.start_time, instance.finish_time):
            raise ValidationError('Booking time overlaps with an existing booking.')

        return instance

    def to_representation(self, instance):
        if not is_valid_actual(instance.date, instance.finish_time):
            instance.active = False

        return super().to_representation(instance)

    def create(self, validated_data):
        if not is_valid_actual(validated_data['date'], validated_data['start_time']):
            raise ValidationError('Stages can not be booked on the past time.')

        if are_overlapping(validated_data):
            raise ValidationError('Booking time overlaps with an existing booking.')

        return create_booking(self.context['request'].user, validated_data)

