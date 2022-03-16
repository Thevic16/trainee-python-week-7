from django.contrib import admin

# Register your models here.
from rent.models import Rent


class RentAdmin(admin.ModelAdmin):
    search_fields = ['client__person__name', 'client__person__lastname',
                     'film__title']
    readonly_fields = ['cost']
    raw_id_fields = ['film', 'client']

    def cost(self, obj, *arg, **kwargs):
        return str(obj.cost)


admin.site.register(Rent, RentAdmin)
