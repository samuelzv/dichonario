from django.utils.translation import gettext
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from django.db.models import Q

from ..domain.util import get_command_buttons, set_session_action, paginate_list
from ..domain.paginate_results import Paginated, PaginatedResults, paginate_results
from ..domain.i18n import get_i18n_quotes_list
from ..domain.constants import command_buttons, sections
from django.template import RequestContext

from django.core import serializers
from ..domain.quote_list_factory import QuoteListFactory
from django.http import JsonResponse


from ..models import Quote
from ..forms import QuoteForm
from ..domain.quote_session import QuoteSession, QuoteScope
from ..selectors import (
    quote_delete_by_id,
    quote_list_created_by,
    quote_list_public,
    author_by_id,
    language_by_code,
    get_author_list,
    quote_by_id,
    get_favorite_quote_from_user,
)

from ..services import quote_create, quote_update, author_create, favorite_create
from ..forms import RegistrationForm
from django.contrib.auth import login


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("quote-main-public")
    else:
        form = RegistrationForm()

    return render(request, "registration/signup.html", {"form": form})


def home(request):
    quote_list_factory = QuoteListFactory().create("welcome")
    quotes = quote_list_factory.quotes()
    [welcome] = quotes

    return render(
        request,
        "quotes/home.html",
        {
            "quote": welcome,
        },
    )


def quote_public(request):
    return get_quotes(request, "public")


@login_required
def quote_mine(request):
    return get_quotes(request, "mine")


def get_quotes(request, section: str):
    search = request.GET.get("search", "")
    current_page = int(request.GET.get("page", "1"))

    filters = {"user": request.user, "search": search}
    quote_list_factory = QuoteListFactory().create(section)
    quotes = quote_list_factory.quotes(**filters)

    paginated = Paginated(queryset=quotes, current_page=current_page, page_size=3)
    paginated_results = paginated.paginate()

    ctx = {
        "search": search,
        "section": section,
        "paginated_results": paginated_results,
        "current_page": current_page,
        "view_name": "quote-main-%s" % section,
    }

    if "HX-Request" in request.headers:
        if request.GET.get("chunk", ""):
            return render(request, "quotes/partials/quote_list_chunk.html", context=ctx)
        else:
            return render(request, "quotes/partials/quote_list.html", context=ctx)

    return render(request, "quotes/quote_main_list.html", context=ctx)


@login_required
def quote_new(request):
    authors = get_author_list()

    if request.method == "POST":
        author_id = request.POST.get("author")
        # there's no author id, so user tries to create a new one,
        # use then the author_text value
        if not author_id:
            author = author_create(
                name=request.POST.get("author_text"), created_by=request.user
            )
            form = QuoteForm(
                {
                    "quote": request.POST.get("quote"),
                    "author": author.id,
                    "is_private": request.POST.get("is_private"),
                }
            )
        else:
            author = author_by_id(id=author_id)
            form = QuoteForm(request.POST)

        if form.is_valid():
            quote_create(
                quote=form.cleaned_data["quote"],
                author=author,
                created_by=request.user,
                is_private=form.cleaned_data["is_private"],
                language=language_by_code(code=request.LANGUAGE_CODE),
            )

            return redirect("quote-main-mine")
    else:
        form = QuoteForm()

    ctx = {
        "form": form,
        "title": gettext("New"),
        "authors": authors,
        "command_buttons": command_buttons,
        "selected_command": "new",
        "success_url": "home",
    }

    if "HX-Request" in request.headers:
        return render(request, "quotes/partials/quote_new.html", context=ctx)

    return render(
        request,
        "quotes/quote_new.html",
        context=ctx,
    )


def quote_partial_toggle_favorite(request, pk):
    is_favorite = False
    quote = quote_by_id(id=pk)
    favorite = get_favorite_quote_from_user(
        quote=quote,
        created_by=request.user,
    )
    if favorite is None:
        favorite_create(
            quote=quote,
            created_by=request.user,
        )
        is_favorite = True
    else:
        favorite.delete()

    return render(
        request,
        "quotes/partials/favorite.html",
        {
            "quote_id": pk,
            "is_favorite": is_favorite,
        },
    )


def quote_partial_edit(request, pk):
    quote = quote_by_id(id=pk)
    author = None

    if request.method == "POST":
        author_id = request.POST.get("author")
        if not author_id:
            # theres no author, so try to  create a new one
            author = author_create(
                name=request.POST.get("author_text"), created_by=request.user
            )
            form = QuoteForm(
                {
                    "quote": request.POST.get("quote"),
                    "author": author.id,
                    "is_private": request.POST.get("is_private"),
                },
                instance=quote,
            )
        else:
            author = author_by_id(id=author_id)
            form = QuoteForm(request.POST)

        if form.is_valid():
            quote_update(
                id=pk,
                quote=form.cleaned_data["quote"],
                author=form.cleaned_data["author"],
                is_private=form.cleaned_data["is_private"],
            )

            return redirect("quote-partial-show", pk=pk)
            # return HttpResponseRedirect(next)
    else:
        form = QuoteForm(instance=quote)

    authors = get_author_list()
    return render(
        request,
        "quotes/partials/quote_edit.html",
        {
            "form": form,
            "title": gettext("Edit"),
            "quote": quote,
            "authors": authors,
            "editable": request.user.is_authenticated
            and quote.created_by == request.user,
        },
    )


def quote_partial_show(request, pk):
    quote = quote_by_id(id=pk)

    ctx = {
        "quote": quote,
        "editable": request.user.is_authenticated and quote.created_by == request.user,
    }

    return render(
        request,
        "quotes/partials/quote_show.html",
        context=ctx,
    )


def quote_partial_delete(request, pk):
    quote = quote_by_id(id=pk)

    return render(
        request,
        "quotes/partials/quote_delete.html",
        {
            "quote": quote,
            "editable": request.user.is_authenticated
            and quote.created_by == request.user,
        },
    )


def quote_partial_confirm_delete(request, pk):
    quote = quote_delete_by_id(id=pk)

    return redirect("quote-main-mine")


def exit(request):
    logout(request)

    return redirect("home")
