from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.template.loader import render_to_string
# from weasyprint import HTML
from .models import *
from .serializers import *

class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

class HeroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filterset_fields = ['category', 'is_visible']
    ordering_fields = ['order']

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.filter(is_visible=True)
    serializer_class = ExperienceSerializer
    ordering_fields = ['order', 'start_date']

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_visible=True)
    serializer_class = ProjectSerializer
    ordering_fields = ['order']

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.filter(is_visible=True)
    serializer_class = EducationSerializer
    ordering_fields = ['order']

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

class CVViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def ats_pdf(self, request):
        return Response({"error": "PDF generation requires system libraries (Gtk+) not found in this environment. Please refer to WeasyPrint documentation for Windows."}, status=500)
        # site = SiteSettings.objects.first()
        # ... (rest commented out)
