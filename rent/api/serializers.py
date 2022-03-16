from rest_framework import serializers
from django.db import models
from rent.models import Rent
from rest_framework.reverse import reverse as api_reverse


class RentSerializer(serializers.ModelSerializer):
    cost = serializers.ReadOnlyField()

    class Meta:
        model = Rent
        fields = [
            'id',
            'film',
            'client',
            'amount',
            'start_date',
            'return_date',
            'actual_return_date',
            'state',
            'cost',
        ]

    def get_uri(self, obj: models.Model, model_name: str, app_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'{app_name}:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['film'] = self.get_uri(instance.film, 'film', 'film')
        response['client'] = self.get_uri(instance.client, 'client', 'person')

        return response
