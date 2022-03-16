from django.contrib import admin

# Register your models here.
from person.models import Person, Role, FilmPersonRole, Client


class PersonAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'lastname',
        'gender',
        'date_of_birth',
        'person_type',
        'age']

    readonly_fields = ['age']
    search_fields = ['name', 'lastname', 'gender', 'person_type']

    def age(self, obj, *arg, **kwargs):
        return str(obj.age)


class RoleAdmin(admin.ModelAdmin):
    search_fields = ['name']


class FilmPersonRoleAdmin(admin.ModelAdmin):
    search_fields = ['film__title', 'person__name',
                     'person__lastname', 'role__name']
    raw_id_fields = ['film', 'person', 'role']


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['person__name',
                     'person__lastname', 'phone', 'email']
    raw_id_fields = ['person']


admin.site.register(Person, PersonAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(FilmPersonRole, FilmPersonRoleAdmin)
admin.site.register(Client, ClientAdmin)
