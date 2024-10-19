from django.urls import path, include
from .views import authors, quotes, preferences

urlpatterns = [
    path("", quotes.home, name="home"),
    path('preferences/theme', preferences.theme, name='theme'),
    path("index", quotes.index, name="index"),
    path("list", 
         quotes.QuoteListSvelteTemplateView.as_view(
            page_title="QuoteList", 
            component_name="QuoteList",
        ), 
         name="quote-list"),
    path("list2", quotes.quote_list, name="quote-list-2"),
     path('authors/<int:pk>/update',
         authors.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>', authors.AuthorDetailsView.as_view(), name='author-detail'),
    path("authors", authors.author_list, name="author-list"),
    path("new", quotes.quote_new, name="quote-new"),
    path("quote/<int:pk>/edit-old", quotes.quote_edit_old, name="quote-edit-old"),
    path("quote/<int:pk>/edit", quotes.quote_edit, name="quote-edit"),
    path(
        "quote/<int:pk>/delete", quotes.QuoteDeleteView.as_view(), name="quote-delete"
    ),
    path("logout/", quotes.exit, name="exit"),
    path("signup/", quotes.signup, name="signup"),
]
