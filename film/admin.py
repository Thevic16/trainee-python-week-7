from django.contrib import admin
from film.models import Film, Category, Season, Chapter


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class FilmAdmin(admin.ModelAdmin):
    search_fields = ['title', 'release_date', 'category__name', 'film_type']
    raw_id_fields = ['film_prequel']


class SeasonAdmin(admin.ModelAdmin):
    search_fields = ['title']
    raw_id_fields = ['film', 'season_prequel']


class ChapterAdmin(admin.ModelAdmin):
    search_fields = ['title']
    raw_id_fields = ['season', 'chapter_prequel']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Chapter, ChapterAdmin)
