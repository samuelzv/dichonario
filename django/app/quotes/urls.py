from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
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
