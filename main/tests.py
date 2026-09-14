from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Achievement
import datetime

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")


# Unittest buat achievement page
class AchievementPageTest(TestCase):
    
    def test_url_and_template_correct(self):
        # Apakah url bisa diakses pake template yang bener
        response = self.client.get(reverse('main:show_achievement'))
        
        self.assertEqual(response.status_code, 200) # 200 artinya OK
        self.assertTemplateUsed(response, 'achievement.html')

    def test_model_data_appears_when_data_exists(self):
        # Bikin dummy data dulu
        Achievement.objects.create(
            title="1st Place AI Challenge",
            organizer="COMPFEST 18",
            achieved_at=datetime.date(2026, 4, 1)
        )
        
        response = self.client.get(reverse('main:show_achievement'))
        
        # Apakah terender di page?
        self.assertContains(response, "1st Place AI Challenge")
        self.assertContains(response, "COMPFEST 18")

    def test_empty_state_message_when_no_data(self):
        # Sengaja ga buat data dummy biar kosong
        response = self.client.get(reverse('main:show_achievement'))
        self.assertContains(response, "Belum ada achievement saat ini.")