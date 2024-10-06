from django.urls import path, include
from . import views
from .views import QuoteListSvelteTemplateView 

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("list", 
         QuoteListSvelteTemplateView.as_view(
            page_title="QuoteList", 
            component_name="QuoteList",
        ), 
         name="quote-list"),
    path("list2", views.quote_list, name="quote-list-2"),
     path('authors/<int:pk>/update',
         views.AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>', views.AuthorDetailsView.as_view(), name='author-detail'),
    path("authors", views.author_list, name="author-list"),
    path("new", views.quote_new, name="quote-new"),
    path("quote/<int:pk>/edit", views.quote_edit, name="quote-edit"),
    path(
        "quote/<int:pk>/delete", views.QuoteDeleteView.as_view(), name="quote-delete"
    ),
    path("logout/", views.exit, name="exit"),
    path("signup/", views.signup, name="signup"),
]
