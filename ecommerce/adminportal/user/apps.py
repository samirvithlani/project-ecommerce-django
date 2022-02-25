from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'adminportal.user'

    def ready(self):
        import adminportal.user.signals
