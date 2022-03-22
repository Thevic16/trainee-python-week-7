from django.db.models import Q
from django.utils.decorators import method_decorator
from rest_framework import generics, mixins

from account.api.permissions import ReadOnly, IsAdmin
from person.api.serializers import (PersonSerializer, RoleSerializer,
                                    FilmPersonRoleSerializer, ClientSerializer)
from person.models import Person, Role, FilmPersonRole, Client
from django.core.exceptions import ValidationError
from rest_framework.response import Response

# Views Person
from utilities.logger import Logger

from film_rental_system.settings import CACHE_TTL
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie


class PersonAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

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


class PersonAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    ordering_fields = ('id', 'name', 'lastname', 'date_of_birth')
    search_fields = ('id', 'name', 'lastname', 'gender', 'date_of_birth',
                     'person_type')

    def get_queryset(self):
        request = self.request
        qs = Person.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(name__icontains=query) |
                           Q(lastname__icontains=query) |
                           Q(person_type__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super(PersonAPIView, self).get(request, *args, **kwargs)


# Views Role
class RoleAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

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


class RoleAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    ordering_fields = ('id', 'name')
    search_fields = ('id', 'name', 'description')

    def get_queryset(self):
        request = self.request
        qs = Role.objects.all()
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
        return super(RoleAPIView, self).get(request, *args, **kwargs)


# Views FilmPersonRole
class FilmPersonRoleAPIDetailView(mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = FilmPersonRoleSerializer
    queryset = FilmPersonRole.objects.all()

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


class FilmPersonRoleAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = FilmPersonRole.objects.all()
    serializer_class = FilmPersonRoleSerializer
    ordering_fields = ('id', 'film__title', 'person__name', 'person__lastname',
                       'role__name')
    search_fields = ('id', 'film__title', 'person__name', 'person__lastname',
                     'role__name')

    def get_queryset(self):
        request = self.request
        qs = FilmPersonRole.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(film_title__icontains=query) |
                           Q(person_name__icontains=query) |
                           Q(person_lastname__icontains=query) |
                           Q(person_role__name__icontains=query)
                           )
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
        return super(FilmPersonRoleAPIView, self).get(request, *args, **kwargs)


# Views Client
class ClientAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                          generics.RetrieveAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

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


class ClientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [ReadOnly | IsAdmin]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    ordering_fields = ('id', 'person__name', 'person__lastname', 'phone',
                       'email')
    search_fields = ('id', 'person__name', 'person__lastname',
                     'direction', 'phone', 'email')

    def get_queryset(self):
        request = self.request
        qs = Client.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(person_name__icontains=query) |
                           Q(person_lastname__icontains=query))
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
        return super(ClientAPIView, self).get(request, *args, **kwargs)
