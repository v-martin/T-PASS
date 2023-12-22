from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Stage, Booking, Service
from services.infrastructure.api_db import create_booking, get_all_services, get_all_stages
from services.domain.schedule import is_valid_actual, check_constraints


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(many=True, queryset=get_all_services())

    class Meta:
        model = Stage
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = '__all__'

    # Update a booking instance. Validates time constraints.
    def update(self, instance, validated_data):
        instance.stage = validated_data.get('stage', instance.stage)
        instance.date = validated_data.get('date', instance.date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.finish_time = validated_data.get('finish_time', instance.finish_time)
        instance.active = validated_data.get('active', instance.active)

        if not is_valid_actual(instance.date, instance.start_time):
            raise ValidationError('Stages can not be booked on the past time.')

        if check_constraints({'stage': instance.stage, 'date': instance.date,
                              'start_time': instance.start_time, 'finish_time': instance.finish_time}):
            return instance

    # Represent a booking instance. Deactivates if finish time is in the past.
    def to_representation(self, instance):
        if not is_valid_actual(instance.date, instance.finish_time):
            instance.active = False

        return super().to_representation(instance)

    # Create a booking instance. Validates time constraints.
    def create(self, validated_data):
        if not is_valid_actual(validated_data['date'], validated_data['start_time']):
            raise ValidationError('Stages can not be booked on the past time.')

        if not check_constraints(validated_data):
            raise ValidationError('Booking constraints are not fulfilled.')

        if 'request' not in self.context and not self.context['request'].user:
            raise ValidationError('Could not resolve user of the booking.')

        return create_booking(self.context['request'].user, validated_data)
