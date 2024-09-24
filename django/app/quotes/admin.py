from django.contrib import admin
from .models import Author, Language, Quote


class QuoteAdmin(admin.ModelAdmin):
    fields = ('author', 'language', 'quote', 'created_by', 'is_private')
    list_display = ('author', 'language', 'quote',
                    'is_private', 'created_by', 'created_at')
    list_filter = ('author', 'language')
    search_fields = ('quote', 'author__name', 'language__name')
    date_hierarchy = 'created_at'


# Register your models here.
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Quote, QuoteAdmin)
