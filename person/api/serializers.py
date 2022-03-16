from rest_framework import serializers
from person.models import Person, FilmPersonRole, Role, Client
from django.db import models
from rest_framework.reverse import reverse as api_reverse


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()

    class Meta:
        model = Person
        fields = [
            'id',
            'name',
            'lastname',
            'gender',
            'date_of_birth',
            'person_type',
            'age',
        ]


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'description',
        ]


class FilmPersonRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmPersonRole
        fields = [
            'id',
            'film',
            'person',
            'role',
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
        response['person'] = self.get_uri(instance.person, 'person', 'person')
        response['role'] = self.get_uri(instance.role, 'role', 'person')
        return response


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'person',
            'direction',
            'phone',
            'email',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'person:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['person'] = self.get_uri(instance.person, 'person')
        return response
