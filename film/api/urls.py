from django.urls import path

from film.api.views import (FilmAPIDetailView, FilmAPIView, CategoryAPIView,
                            CategoryAPIDetailView, SeasonAPIView,
                            SeasonAPIDetailView, ChapterAPIView,
                            ChapterAPIDetailView)
app_name = 'film'

urlpatterns = [
    # Paths category
    path('category/', CategoryAPIView.as_view()),
    path('category/<int:pk>/', CategoryAPIDetailView.as_view(),
         name='category-detail'),
    # Paths film
    path('film/', FilmAPIView.as_view()),
    path('film/<int:pk>/', FilmAPIDetailView.as_view(), name='film-detail'),
    # Paths season
    path('season/', SeasonAPIView.as_view()),
    path('season/<int:pk>/', SeasonAPIDetailView.as_view(),
         name='season-detail'),
    # Paths chapter
    path('chapter/', ChapterAPIView.as_view()),
    path('chapter/<int:pk>/', ChapterAPIDetailView.as_view(),
         name='chapter-detail'),
]
