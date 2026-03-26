from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'settings', SiteSettingsViewSet)
router.register(r'hero', HeroViewSet)
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experience', ExperienceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'education', EducationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cv/ats.pdf', CVViewSet.as_view({'get': 'ats_pdf'}), name='cv-pdf'),
]
