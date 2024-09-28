from django.urls import path, include
from . import views
from .views import MySvelteTemplateView, MyContextSvelteTemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    # path("list2", views.quote_list2, name="quote-list2"),
    path("list2", 
         MySvelteTemplateView.as_view(
            page_title="QuoteList", component_name="QuoteList"
        ), 
         name="quote-list2"),
    path("list", views.quote_list, name="quote-list"),
    path("authors", views.author_list, name="author-list"),
    path("new", views.quote_new, name="quote-new"),
    path("quote/<int:pk>/edit", views.quote_edit, name="quote-edit"),
    path(
        "quotes/<int:pk>/delete", views.QuoteDeleteView.as_view(), name="quote-delete"
    ),
    path("logout/", views.exit, name="exit"),
    path("signup/", views.signup, name="signup"),
]
