from django.apps import AppConfig


class RegistryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.registry'
    verbose_name = 'Реєстр медіаторів'

    def ready(self):
        import apps.registry.signals
