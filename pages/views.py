from django.views.generic import TemplateView
from drivingschool.models import UserProfile


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aos_effects = [
            "fade",
            "fade-down",
            "fade-down-left",
            "fade-down-right",
            "fade-left",
            "fade-right",
            "fade-up",
            "fade-up-left",
            "fade-up-right",
            "flip-down",
            "flip-left",
            "flip-right",
            "flip-up",
            "slide-down",
            "slide-left",
            "slide-right",
            "slide-up",
            "zoom-in",
            "zoom-in-down",
            "zoom-in-left",
            "zoom-in-right",
            "zoom-in-up",
            "zoom-out",
            "zoom-out-down",
            "zoom-out-left",
            "zoom-out-right",
            "zoom-out-up",
        ]
        image_numbers = [
            19,
            18,
            17,
            16,
            15,
            14,
            13,
            12,
            11,
            10,
            9,
            8,
            7,
            6,
            5,
            4,
            3,
            2,
            1,
        ]
        image_urls = [
            f"images/home/{image_number}.webp" for image_number in image_numbers
        ]
        context["image_urls"] = image_urls
        context["aos_effects"] = aos_effects
        if self.request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=self.request.user)
            context["user_role"] = user_profile.user_type
            context["full_name"] = user_profile.full_name
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
