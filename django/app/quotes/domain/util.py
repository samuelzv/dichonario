from django.urls import reverse
from .constants import command_buttons
import copy

def setUrlButton(button):
    button["url"] = reverse(button["url"]) + "?action=" + button["id"]
    return button

def get_command_buttons():
    return list(map(setUrlButton, copy.deepcopy(command_buttons)))



