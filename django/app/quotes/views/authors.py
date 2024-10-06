from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView
from django.db.models import Q

from ..selectors import get_author_list_count_quotes 
from ..models import Author
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage
from ..domain.util import get_command_buttons, is_authorizer
from ..domain.constants import command_buttons

@login_required
def author_list(request):
    authors = get_author_list_count_quotes()

    ### set_session_action(request)
    return render(
        request,
        "quotes/author_list.html",
        {
            "command_buttons": command_buttons,
            "selected_command": request.session["action"],
            "authors": authors,
            "is_authorizer": is_authorizer(request.user)
        },
    )

@method_decorator(login_required, name='dispatch')
class AuthorDetailsView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if is_authorizer(self.request.user):
            author_quotes = context['author'].quotes.all()
        else:
            author_quotes = context['author'].quotes.filter(
                Q(authorized=True) |
                Q(created_by=self.request.user)
            )

        paginator = Paginator(author_quotes, 1)

        try:
            current_page = self.request.GET.get('page', 1)
            quotes = paginator.page(current_page)
        except EmptyPage:
            quotes = paginator.page(1)
            current_page = 1

        context['quotes'] = quotes
        context['is_authorizer'] = is_authorizer(self.request.user)
        context['is_author_creator'] = context['author'].created_by == self.request.user
        context['current_page'] = current_page

        return context

class AuthorUpdateView(UserPassesTestMixin, UpdateView):
    model = Author
    fields = ['name', 'image']
    context_object_name = 'author'

    def test_func(self):
        return is_authorizer(self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # if not is_authorizer(self):
            # form.fields.pop('authorized')

        return form
