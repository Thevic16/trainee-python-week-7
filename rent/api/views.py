from django.db.models import Q
from rest_framework import generics, mixins
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rent.api.serializers import RentSerializer
from rent.models import Rent
from utilities.logger import Logger


class RentAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = RentSerializer
    queryset = Rent.objects.all()

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


class RentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    ordering_fields = ('id', 'client__person__name',
                       'client__person__lastname', 'amount', 'start_date',
                       'return_date', 'actual_return_date')
    search_fields = ('id', 'client__person__name', 'client__person__lastname',
                     'amount', 'start_date', 'return_date',
                     'actual_return_date', 'state')

    def get_queryset(self):
        request = self.request
        qs = Rent.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(film__title__icontains=query) |
                           Q(person_name__icontains=query) |
                           Q(person_lastname__icontains=query) |
                           Q(state__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except ValidationError as e:
            Logger.debug(f'ValidationError:{e}')
            return Response(e)
