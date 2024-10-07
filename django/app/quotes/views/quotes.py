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

from ..domain.util import get_command_buttons , set_session_action
from ..domain.paginate_results import paginate_results
from ..domain.i18n import get_i18n_quotes_list
from ..domain.constants import command_buttons
from django.template import RequestContext

from django.core import serializers
from ..domain.quote_list_factory import QuoteListFactory


from ..models import Quote
from ..forms import QuoteForm
from ..domain.quote_session import QuoteSession, QuoteScope
from ..selectors import (
    quote_list_created_by,
    quote_list_public,
    author_by_id,
    language_by_code,
    get_author_list,
    quote_by_id,
)
from ..services import quote_create, quote_update, author_create
from ..forms import RegistrationForm
from django.contrib.auth import login

from django_svelte.views import SvelteTemplateView

class QuotesBaseSvelteTemplateView(SvelteTemplateView):
    template_name = "quotes/svelte_component.html"

    def get_svelte_props(self, **kwargs):
        return kwargs


class QuoteListSvelteTemplateView(QuotesBaseSvelteTemplateView):
    def get_svelte_props(self, **kwargs):
        set_session_action(self.request)
        filters = {
            'user': self.request.user, 
            'search': self.request.session["search"]
        }
        action = self.request.session["action"]
        quote_list_factory = QuoteListFactory().create(action)

        quote_list = quote_list_factory.quotes(**filters).values('id','quote', 'author__name', 'author__image', 'created_by')
        (quotes, pagination) = paginate_results(quote_list, int(self.request.GET.get("page", 1)), 15)
        
        for q in quotes:
            q['is_owner'] = q['created_by'] == self.request.user.id

        kwargs.update({
            "command_buttons": get_command_buttons(),
            "i18n": get_i18n_quotes_list(),
            "quotes": quotes,
            "search": self.request.GET.get("search", ""),
            "selected_command": action, 
            'pagination': pagination,
            'quote_list_url': reverse('quote-list'),
            'quote_new_url': reverse('quote-new'),
            'language_code': self.request.LANGUAGE_CODE,
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
    return render(request, 
                  "quotes/home.html", 
                  {
                    "component_props": {
                        "text": "Welcome to Dichonario, the place for gathering and sharing your favorite quotes"
                    } 
                  })


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

            return redirect("quote-list")
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
class QuoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Quote

    def test_func(self):
        return self.get_object().created_by == self.request.user

    def get_success_url(self) -> str:
        next = self.request.GET.get("next")
        return next if next else reverse("quote-list")




def exit(request):
    logout(request)

    return redirect("home")
