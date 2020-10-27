from django.db.models.base import Model
from django.db.models.constraints import CheckConstraint
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField
from django.db.models.query_utils import Q

from django.utils.translation import gettext_lazy as _


class Title(TextChoices):
    DEDICATED_TRANSPORT = "Dedicated Transport", _("Dedicated Transport")
    ELITES = "Elites", _("Elites")
    FAST_ATTACK = "Fast Attack", _("Fast Attack")
    FLYER = "Flyer", _("Flyer")
    FORTIFICATION = "Fortification", _("Fortification")
    HEAVY_SUPPORT = "Heavy Support", _("Heavy Support")
    HQ = "HQ", _("HQ")
    LORD_OF_WAR = "Lord of War", _("Lord of War")
    TROOPS = "Troops", _("Troops")


class BattlefieldRole(Model):
    title = CharField(_("title"), choices=Title.choices, db_index=True, max_length=19, unique=True)

    class Meta:
        constraints = (
            CheckConstraint(check=Q(title__in=Title.values), name="%(app_label)s_%(class)s_title_valid"),
            CheckConstraint(check=Q(pk__in=range(1, 10)), name="%(app_label)s_%(class)s_objects_count_valid"),
        )
        verbose_name = _("battlefield role")
        verbose_name_plural = _('battlefield roles')

    def __str__(self):
        return self.title
