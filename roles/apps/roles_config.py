from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RolesConfig(AppConfig):
    name = 'roles'
    verbose_name = _("Roles")
