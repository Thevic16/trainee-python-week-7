from django.urls import path
from person.api.views import (PersonAPIDetailView, PersonAPIView, RoleAPIView,
                              RoleAPIDetailView, FilmPersonRoleAPIView,
                              FilmPersonRoleAPIDetailView, ClientAPIView,
                              ClientAPIDetailView)

app_name = 'person'

urlpatterns = [
    # Paths Person
    path('person/', PersonAPIView.as_view()),
    path('person/<int:pk>/', PersonAPIDetailView.as_view(),
         name='person-detail'),
    # Paths Role
    path('role/', RoleAPIView.as_view()),
    path('role/<int:pk>/', RoleAPIDetailView.as_view(),
         name='role-detail'),
    # Paths film-person-role
    path('film-person-role/', FilmPersonRoleAPIView.as_view()),
    path('film-person-role/<int:pk>/', FilmPersonRoleAPIDetailView.as_view(),
         name='film-person-role-detail'),
    # Paths Client
    path('client/', ClientAPIView.as_view()),
    path('client/<int:pk>/', ClientAPIDetailView.as_view(),
         name='client-detail'),
]
