from django.apps import AppConfig


class TenantsConfig(AppConfig):
    name = 'tenants'

    def ready(self):
        import tenants.signals

