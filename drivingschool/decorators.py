from django.shortcuts import redirect

from .models import UserProfile


def redirect_secretary(function):
    def wrap(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.user_type == "Secretary":
            return redirect("general_schedule")
        else:
            return function(request, *args, **kwargs)

    return wrap
