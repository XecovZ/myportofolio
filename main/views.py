from main.models import Experience, Project
from main.models import Achievement

from main.forms import AchievementForm, ExperienceForm, ProjectForm
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

import datetime

from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini


# Cek status EDITOR
def is_editor(user):
    return user.groups.filter(name='Editor').exists()


# REGISTRATION
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "M. Fatih Danika",
        "form": form,
    }
    return render(request, "register.html", context)


# LOGIN
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "M. Fatih Danika",
        "form": form,
    }
    return render(request, "login.html", context)


# LOGOUT
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response


# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "M. Fatih Danika",
        "npm": "2506532100",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "TA & CS Undergraduate Student @ Universitas Indonesia. Exploring Data Science & Artificial Intelligence."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


# EXPERIENCE

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [exp.object for exp in experiences]
    title_query = request.GET.get("title", "").strip()
    
    user_is_editor = False
    if request.user.is_authenticated:
        user_is_editor = is_editor(request.user)
    
    context = {
        "name": "M. Fatih Danika",
        "experience_list": experiences,
        "title_query": title_query,
        "is_editor_flag": user_is_editor,
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "M. Fatih Danika",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diubah!")
        return redirect("main:show_experience")
    
    context = {
        "name": "M. Fatih Danika",
        "form": form, 
        "is_edit": True,
    }
    return render(request, "experience_form.html", context)


# ACHIEVEMENT

def show_achievement(request):
    json_response = get_achievement_json(request)
    achievements = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    achievements = [ach.object for ach in achievements]
    title_query = request.GET.get("title", "").strip()
    
    user_is_editor = False
    if request.user.is_authenticated:
        user_is_editor = is_editor(request.user)
    
    context = {
        "name": "M. Fatih Danika",
        "achievement_list": achievements,
        "title_query": title_query,
        "is_editor_flag": user_is_editor,
    }
    return render(request, "achievement.html", context)


@login_required(login_url="/login/")
def create_achievement(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = AchievementForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Achievement baru berhasil ditambahkan!")
        return redirect("main:show_achievement")

    context = {
        "name": "M. Fatih Danika",
        "form": form,
    }
    return render(request, "achievement_form.html", context)


def get_achievement_json(request):
    title_query = request.GET.get("title", "").strip()
    achievement = Achievement.objects.all()

    if title_query:
        achievement = achievement.filter(title__icontains=title_query)

    achievement_json = serializers.serialize("json", achievement)
    return HttpResponse(achievement_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_achievement(request, achievement_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == "POST":
        achievement.delete()
        messages.success(request, "Achievement berhasil dihapus!")
        return redirect("main:show_achievement")

    return redirect("main:show_achievement")


@login_required(login_url="/login/")
def edit_achievement(request, achievement_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    form = AchievementForm(request.POST or None, instance=achievement)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Achievement berhasil diubah!")
        return redirect("main:show_achievement")
    
    context = {
        "name": "M. Fatih Danika",
        "form": form, 
        "is_edit": True,
    }
    return render(request, "achievement_form.html", context)


# PROJECTS

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    
    user_is_editor = False
    if request.user.is_authenticated:
        user_is_editor = is_editor(request.user)

    context = {
        "name": "M. Fatih Danika",
        "project_list": projects,
        "title_query": title_query,
        "is_editor_flag": user_is_editor,
    }
    return render(request, "project.html", context)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "M. Fatih Danika",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True  # Tambahkan argumen ini
    )
    return HttpResponse(projects_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")


@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diubah!")
        return redirect("main:show_projects")
    
    context = {
        "name": "M. Fatih Danika",
        "form": form, 
        "is_edit": True,
    }
    return render(request, "projects_form.html", context)


# Star feature

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")