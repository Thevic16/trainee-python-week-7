from rest_framework import serializers
from film.models import Film, Category, Season, Chapter
from django.db import models
from rest_framework.reverse import reverse as api_reverse


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
        ]


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = [
            'id',
            'title',
            'description',
            'release_date',
            'category',
            'price_by_day',
            'stock',
            'availability',
            'film_type',
            'film_prequel',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'film:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = self.get_uri(instance.category, 'category')
        response['film_prequel'] = self.get_uri(instance.film_prequel,
                                                'film')
        return response


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = [
            'id',
            'film',
            'title',
            'season_prequel',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'film:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['film'] = self.get_uri(instance.film, 'film')
        response['season_prequel'] = self.get_uri(instance.season_prequel,
                                                  'season')
        return response


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            'id',
            'season',
            'title',
            'chapter_prequel',
        ]

    def get_uri(self, obj: models.Model, model_name: str):
        request = self.context.get('request')
        if obj is not None:
            return api_reverse(f'film:{model_name}-detail',
                               kwargs={'pk': obj.id}, request=request)
        else:
            return '--------'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['season'] = self.get_uri(instance.season, 'season')
        response['chapter_prequel'] = self.get_uri(instance.chapter_prequel,
                                                   'chapter')
        return response
