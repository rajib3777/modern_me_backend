import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Hero

hero = Hero.objects.first()
if hero:
    hero.image = 'hero/developer_profile.png'
    hero.save()
    print(f"Updated hero image to: {hero.image}")
else:
    print("No Hero object found.")
