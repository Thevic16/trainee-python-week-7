from django.urls import path
from person.api.views import (PersonAPIDetailView, PersonAPIView, RoleAPIView,
                              RoleAPIDetailView, FilmPersonRoleAPIView,
                              FilmPersonRoleAPIDetailView, ClientAPIView,
                              ClientAPIDetailView)

app_name = 'person'

urlpatterns = [
    # Paths Person
    path('persons/', PersonAPIView.as_view()),
    path('persons/<int:pk>/', PersonAPIDetailView.as_view(),
         name='person-detail'),
    # Paths Role
    path('roles/', RoleAPIView.as_view()),
    path('roles/<int:pk>/', RoleAPIDetailView.as_view(),
         name='role-detail'),
    # Paths film-person-role
    path('films-persons-roles/', FilmPersonRoleAPIView.as_view()),
    path('films-persons-roles/<int:pk>/',
         FilmPersonRoleAPIDetailView.as_view(),
         name='film-person-role-detail'),
    # Paths Client
    path('clients/', ClientAPIView.as_view()),
    path('clients/<int:pk>/', ClientAPIDetailView.as_view(),
         name='client-detail'),
]
