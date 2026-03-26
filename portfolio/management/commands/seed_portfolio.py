from django.core.management.base import BaseCommand
from portfolio.models import *
import datetime

class Command(BaseCommand):
    help = 'Seed the database with real professional data of MD. RAJIBUL ISLAM SHUVO'

    def handle(self, *args, **kwargs):
        self.stdout.write('Initializing Personal Nexus Sequence for Rajibul Shuvo...')

        # Clear existing data
        SiteSettings.objects.all().delete()
        Hero.objects.all().delete()
        About.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Education.objects.all().delete()

        # Site Settings
        SiteSettings.objects.create(
            brand_name="RAJIBUL.V3",
            tagline="Full-Stack Developer | Scaling Digital Solutions",
            primary_color="#06b6d4",
            secondary_color="#020617",
            contact_email="rajibulislam3777@gmail.com"
        )

        # Hero
        Hero.objects.update_or_create(
            id=1,
            defaults={
                "headline": "MD. RAJIBUL ISLAM SHUVO",
                "subheadline": "Full-Stack Developer with hands-on experience in Django REST Framework, React, PostgreSQL, and production deployment. Dedicated to building efficient, scalable software solutions.",
                "cta_text": "DOWNLOAD CV",
                "github_url": "https://github.com",
                "linkedin_url": "https://linkedin.com",
                "twitter_url": "https://twitter.com",
                "image": "hero/profile.jpg"
            }
        )

        # About
        About.objects.update_or_create(
            id=1,
            defaults={
                "title": "Professional Matrix",
                "bio": "Full-Stack Developer skilled in API design, UI development, and problem-solving. Dedicated to continuous learning and building efficient, scalable software solutions with a focus on Django and React ecosystems.",
                "ats_summary": "Full-Stack Developer with hands-on experience in Django REST Framework, React, PostgreSQL, and modern web technologies. Expert in production deployment and scalable architectures.",
                "years_of_experience": 1,
                "projects_completed": 12,
                "happy_clients": 10,
                "image": "about/profile.jpg"
            }
        )

        # Skills
        skill_data = [
            ("Core Frameworks", [("Django / DRF", 95), ("React.js", 90), ("Tailwind CSS", 95)]),
            ("Languages", [("Python", 90), ("JavaScript", 88), ("C / C++", 80)]),
            ("Systems & DB", [("PostgreSQL", 92), ("Postgresql", 92), ("Vercel / Render", 90)]),
            ("Computer Science", [("Algorithm", 85), ("Data structure", 85), ("OOP", 90)]),
        ]
        for cat, skills in skill_data:
            for name, level in skills:
                Skill.objects.create(name=name, category=cat, level=level, is_visible=True)

        # Experience
        Experience.objects.create(
            company="Somadhan Soft",
            role="Internship - Full Stack",
            location="Remote",
            start_date="2025-01-01",
            is_current=True,
            description="Worked on production-grade platforms like VisaFarm and JobsAlign.\nContributing to authentication, API development, and AI-powered job matching.\nImplementing webhook integrations and full-stack features using Django and DRF."
        )

        # Projects
        Project.objects.create(
            title="JOBSALIGN",
            slug="jobsalign",
            description="Scalable freelance platform built with Django REST Framework featuring user authentication, support, live chat, assessments, wallet and notification, and AI-powered job matching.",
            tech_stack="Django, DRF, JWT, Database, Pandas, OOP",
            live_url="https://portfolioteck.vercel.app/",
            repo_url="#",
            order=1
        )

        Project.objects.create(
            title="TRUCKY",
            slug="trucky",
            description="Full-stack logistics app that generates optimized truck routes (ORS/OSRM) and auto-creates FMCSA-compliant HOS log sheets using real-time geocoding.",
            tech_stack="Django, React, Geocoding, Routing",
            live_url="#",
            repo_url="#",
            order=2
        )

        Project.objects.create(
            title="MANGO BAR",
            slug="mango-bar",
            description="Dynamic web application for a juice and dessert shop. Features order management, cart functionality, and responsive Tailwind CSS design.",
            tech_stack="Python, Django, Tailwind CSS, SQLite",
            live_url="#",
            repo_url="#",
            order=3
        )

        Project.objects.create(
            title="EVENT MANAGEMENT SYSTEM",
            slug="event-management",
            description="Full-featured web application to simplify event creation, management, and booking with secure dashboard for admins.",
            tech_stack="DRF, JWT, Database, Pandas, OOP",
            live_url="#",
            repo_url="#",
            order=4
        )

        # Education
        Education.objects.create(
            institute="University of Dhaka",
            degree="BAMS - Department of Pharmacy",
            location="Dhaka, Bangladesh",
            start_year=2021,
            end_year=2025 # Estimated suffix
        )
        
        Education.objects.create(
            institute="Phitron",
            degree="CSE Fundamental Course",
            location="Online",
            start_year=2024,
            end_year=2025
        )

        self.stdout.write(self.style.SUCCESS('Personal Sequence Complete. Rajibul is online.'))
