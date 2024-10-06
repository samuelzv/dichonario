from django.urls import reverse
from .constants import command_buttons
import copy

def setUrlButton(button):
    button["url"] = reverse(button["url"]) + "?action=" + button["id"]
    return button

def get_command_buttons():
    return list(map(setUrlButton, copy.deepcopy(command_buttons)))


def is_authorizer(user):
    return user.groups.filter(name='authorizer').exists()


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
