from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SiteSettings(models.Model):
    brand_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    primary_color = models.CharField(max_length=20, default="#3b82f6")
    secondary_color = models.CharField(max_length=20, default="#1e293b")
    contact_email = models.EmailField()
    logo = models.ImageField(upload_to="site/", null=True, blank=True)

    def __str__(self):
        return self.brand_name

class Hero(models.Model):
    headline = models.CharField(max_length=255)
    subheadline = models.TextField()
    cta_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to="hero/")
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

class About(models.Model):
    title = models.CharField(max_length=200, default="System Architecture")
    bio = models.TextField(default="", help_text="Detailed professional bio")
    ats_summary = models.TextField(default="", help_text="Plain text for ATS")
    years_of_experience = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    image = models.ImageField(upload_to="about/", null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # Dynamic categories for futuristic dashboard
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    level_label = models.CharField(max_length=50, default="Expert")
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Bullet points")
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date', 'order']

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="projects/")
    description = models.TextField(help_text="Rich text")
    ats_description = models.TextField(help_text="Short plain text")
    tech_stack = models.CharField(max_length=255, help_text="Comma separated")
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    details = models.TextField()
    order = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.name}: {self.subject}"
