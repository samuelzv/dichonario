from django.contrib import admin
from .models import Author, Language, Quote, Favorite


class QuoteAdmin(admin.ModelAdmin):
    fields = ("author", "language", "quote", "created_by", "is_private")
    list_display = (
        "author",
        "language",
        "quote",
        "is_private",
        "created_by",
        "created_at",
    )
    list_filter = ("author", "language")
    search_fields = ("quote", "author__name", "language__name")
    date_hierarchy = "created_at"


class FavoriteAdmin(admin.ModelAdmin):
    fields = ("quote", "created_by")
    list_filter = ("created_by",)
    search_fields = ("quote__quote",)


# Register your models here.
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Favorite, FavoriteAdmin)
