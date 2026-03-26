from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ("brand_name", "contact_email")

@admin.register(Hero)
class HeroAdmin(ModelAdmin):
    pass

@admin.register(About)
class AboutAdmin(ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ("name", "category", "level", "order", "is_visible")
    list_editable = ("order", "is_visible")

@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ("role", "company", "start_date", "is_current", "is_visible")
    list_editable = ("is_visible",)

@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ("title", "is_featured", "is_visible", "order")
    list_editable = ("is_featured", "is_visible", "order")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ("degree", "institute", "start_year", "is_visible")

@admin.register(Message)
class MessageAdmin(ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    readonly_fields = ("created_at",)
