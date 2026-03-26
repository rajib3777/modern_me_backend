from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

# Serve static AND media files through Whitenoise in production
if not settings.DEBUG:
    # First, handle static files (usually in STATIC_ROOT)
    application = WhiteNoise(application, root=settings.STATIC_ROOT, prefix=settings.STATIC_URL)
    # Then, add the media folder (where portfolio images are)
    if os.path.exists(settings.MEDIA_ROOT):
        application.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)

app = application
