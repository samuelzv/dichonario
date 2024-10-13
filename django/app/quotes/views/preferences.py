from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse


def theme(request):
    theme = request.POST.get("theme", 'dark')

    response = HttpResponse(
        JsonResponse({'theme': theme}), 
        content_type='application/json')
    response.set_cookie("theme", theme)

    return response
