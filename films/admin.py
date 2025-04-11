from django.contrib import admin
from films.models import Film, Director, Genre, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class FilmAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['name']
    list_filter = ['genres', 'director']
    list_display = ['name', 'director', 'is_active', 'created']

admin.site.register(Film, FilmAdmin)
admin.site.register(Director)
admin.site.register(Genre)
