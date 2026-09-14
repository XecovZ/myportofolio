from django.shortcuts import render

from main.models import Experience
from main.models import Achievement

# Create your views here.
def show_main(request):
    context = {
        "name": "M. Fatih Danika",
        "npm": "2506532100",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "TA & CS Undergraduate Student @ Universitas Indonesia. Exploring Data Science & Artificial Intelligence."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "M. Fatih Danika",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_achievement(request):
    context = {
        "name": "M. Fatih Danika",
        "achievement_list": Achievement.objects.all()
    }
    
    return render(request, "achievement.html", context)