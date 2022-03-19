from django.urls import path

from film.api.views import (FilmAPIDetailView, FilmAPIView, CategoryAPIView,
                            CategoryAPIDetailView, SeasonAPIView,
                            SeasonAPIDetailView, ChapterAPIView,
                            ChapterAPIDetailView)
app_name = 'film'

urlpatterns = [
    # Paths category
    path('categories/', CategoryAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIDetailView.as_view(),
         name='category-detail'),
    # Paths film
    path('films/', FilmAPIView.as_view()),
    path('films/<int:pk>/', FilmAPIDetailView.as_view(), name='film-detail'),
    # Paths season
    path('seasons/', SeasonAPIView.as_view()),
    path('seasons/<int:pk>/', SeasonAPIDetailView.as_view(),
         name='season-detail'),
    # Paths chapter
    path('chapters/', ChapterAPIView.as_view()),
    path('chapters/<int:pk>/', ChapterAPIDetailView.as_view(),
         name='chapter-detail'),
]
