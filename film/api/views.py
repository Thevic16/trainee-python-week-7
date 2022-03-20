from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import generics, mixins
from rest_framework.response import Response

from account.api.permissions import ReadOnly, IsAdmin
from film.models import Film, Category, Season, Chapter
from film_rental_system.settings import CACHE_TTL
from utilities.logger import Logger
from .serializers import (FilmSerializer, CategorySerializer, SeasonSerializer,
                          ChapterSerializer)


# Views Category
class CategoryAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                            generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)


class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering_fields = ('id', 'name')
    search_fields = ('id', 'name', 'description')

    def get_queryset(self):
        request = self.request
        qs = Category.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(name__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super(CategoryAPIView, self).get(request, *args, **kwargs)


# Views Film
class FilmAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = FilmSerializer
    queryset = Film.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)


class FilmAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    ordering_fields = ('id', 'title', 'release_date', 'price_by_day', 'stock',
                       'availability')
    search_fields = ('id', 'title', 'release_date', 'category__name',
                     'film_type')

    def get_queryset(self):
        request = self.request
        qs = Film.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)
                           | Q(category__name__icontains=query)
                           | Q(film_type__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super(FilmAPIView, self).get(request, *args, **kwargs)


# Views Season
class SeasonAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)


class SeasonAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    ordering_fields = ('id', 'title')
    search_fields = ('id', 'film__title', 'title')

    def get_queryset(self):
        request = self.request
        qs = Season.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super(SeasonAPIView, self).get(request, *args, **kwargs)


# Views Chapter
class ChapterAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                           generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def put(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def patch(self, request, *args, **kwargs):
        try:
            return self.update(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)


class ChapterAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    ordering_fields = ('id', 'title')
    search_fields = ('id', 'season__film__title', 'season__title', 'title')

    def get_queryset(self):
        request = self.request
        qs = Chapter.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super(ChapterAPIView, self).get(request, *args, **kwargs)
