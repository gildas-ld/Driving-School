from django.shortcuts import redirect
from django.http import HttpResponseForbidden

from .models import UserProfile


def redirect_secretary(function):
    def wrap(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.user_type == "Secretary":
            return redirect("general_schedule")
        else:
            return function(request, *args, **kwargs)

    return wrap


def secretary_required(function):
    def wrap(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.user_type == "Secretary":
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to view this page.")

    return wrap
