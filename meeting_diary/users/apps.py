from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "meeting_diary.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import meeting_diary.users.signals  # noqa F401
        except ImportError:
            pass
