from django.utils.translation import gettext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from .domain.util import get_command_buttons
from .domain.constants import command_buttons
from django.template import RequestContext

from django.core import serializers


from .models import Quote
from .forms import QuoteForm
from .domain.quote_session import QuoteSession, QuoteScope
from .selectors import (
    quote_list_created_by,
    quote_list_public,
    author_by_id,
    language_by_code,
    get_author_list,
    get_author_list_count_quotes,
    quote_by_id,
)
from .services import quote_create, quote_update, author_create
from .forms import RegistrationForm
from django.contrib.auth import login

from django_svelte.views import SvelteTemplateView


class QuotesBaseSvelteTemplateView(SvelteTemplateView):
    template_name = "quotes/svelte_component.html"

    def get_svelte_props(self, **kwargs):
        return kwargs


class QuoteListSvelteTemplateView(QuotesBaseSvelteTemplateView):
    def get_svelte_props(self, **kwargs):
        quotes = []
        set_session_action(self.request)

        if self.request.session["action"] == "mine":
            quotes = quote_list_created_by(
            user=self.request.user, search=self.request.session["search"]
        )
        else:
            quotes = quote_list_public(self.request.session["search"])

        i18n = {
            'search': gettext('Search'),
            'new_quote': gettext('New quote'),
        }

        kwargs.update({
            "quotes": list(quotes.values('quote', 'author__name')),
            "command_buttons": get_command_buttons(),
            "selected_command": self.request.session["action"],
            "i18n": i18n,
            'quote_list_url': reverse('quote-list'),
            'quote_new_url': reverse('quote-new'),
            })

        return kwargs


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("quote-list")
    else:
        form = RegistrationForm()

    return render(request, "registration/signup.html", {"form": form})


def index(request):
    return render(request, "quotes/index.html")


def home(request):
    return render(request, "quotes/home.html", {"component_props": {"text": "Welcome to Dichonario, the place for gathering and sharing your favorite quotes"} })


def set_session_action(request):
    action = ""
    if request.GET.get("action", "") == "":
        if request.session.get("action", "") == "":
            action = "mine"
        else:
            action = request.session.get("action", "")
    else:
        action = request.GET.get("action", "")

    request.session["action"] = action

    request.session["search"] = request.GET.get("search", "")
    request.session["page"] = request.GET.get("page", 1)

@login_required
def quote_list(request):
    quotes = []
    set_session_action(request)

    if request.session["action"] == "mine":
        quotes = quote_list_created_by(
            user=request.user, search=request.session["search"]
        )
    else:
        quotes = quote_list_public(request.session["search"])

    return render(
        request,
        "quotes/quote_list.html",
        {
            "quotes": quotes,
            "command_buttons": command_buttons,
            "selected_command": request.session["action"],
            "page": request.session["page"],
            "search": request.session["search"],
        },
    )


@login_required
def author_list(request):
    authors = get_author_list_count_quotes()

    set_session_action(request)
    return render(
        request,
        "quotes/author_list.html",
        {
            "command_buttons": command_buttons,
            "selected_command": request.session["action"],
            "authors": authors,
        },
    )


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

            return redirect("home")
    else:
        form = QuoteForm()

    return render(
        request,
        "quotes/quote_new.html",
        {
            "form": form,
            "title": gettext("New"),
            "authors": authors,
            "command_buttons": command_buttons,
            "selected_command": "new",
            "success_url": "home",
        },
    )


def quote_edit(request, pk):
    quote = quote_by_id(id=pk)
    next = request.GET.get("next")
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

            return HttpResponseRedirect(next)
    else:
        form = QuoteForm(instance=quote)

    authors = get_author_list()
    return render(
        request,
        "quotes/quote_edit.html",
        {
            "form": form,
            "title": gettext("Edit"),
            "quote": quote,
            "authors": authors,
            "success_url": next,
            "command_buttons": command_buttons,
            "selected_command": "edit",
        },
    )


@method_decorator(login_required, name="dispatch")
class QuoteDeleteView(DeleteView):
    model = Quote
    success_url = reverse_lazy("quote-list")


def exit(request):
    logout(request)

    return redirect("home")
