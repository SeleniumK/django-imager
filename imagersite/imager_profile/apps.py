from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):
    """Pep 8 told me to."""

    name = 'imager_profile'

    def ready(self):
        """Import handlers on ready."""
        from imager_profile import handlers
