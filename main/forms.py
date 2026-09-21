#from django.forms import *
from django.forms import ModelForm, Select, TextInput, Textarea, URLInput, DateTimeField, DateTimeInput

from main.models import Project, Achievement, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }
        
        
class AchievementForm(ModelForm):
    achieved_at = DateTimeField(
        input_formats=['%Y-%m'],
        widget=DateTimeInput(
            format='%Y-%m',
            attrs={
                "type": "month",
            }
        ),
        label="Waktu didapatkan"
    )
    
    class Meta:
        model = Achievement
        fields = [
            "title",
            "organizer",
            "achieved_at",
        ]

        labels = {
            "title": "Nama Pencapaian",
            "organizer": "Penyelenggara",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Juara 1 GEMASTIK",
                    "maxlength": 255,
                }
            ),
            "organizer": TextInput(
                attrs={
                    "placeholder": "BPTI",
                    "maxlength": 255,
                }
            ),
        }
        
        
class ExperienceForm(ModelForm):
    ended_at = DateTimeField(
        required=False,
        input_formats=['%Y-%m-%d'],
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={
                "type" : "date",
            }
        ),
        label="Waktu berakhir"
    )
    
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Gambar",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }