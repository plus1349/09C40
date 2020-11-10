from django.db.models import CharField, CheckConstraint, Model, TextChoices, Q
from django.utils.translation import gettext_lazy as _


class Title(TextChoices):
    DEDICATED_TRANSPORT = ("Dedicated Transport", "Dedicated Transport",)
    ELITES = ("Elites", "Elites",)
    FAST_ATTACK = ("Fast Attack", "Fast Attack",)
    FLYER = ("Flyer", "Flyer",)
    FORTIFICATION = ("Fortification", "Fortification",)
    HEAVY_SUPPORT = ("Heavy Support", "Heavy Support",)
    HQ = ("HQ", "HQ",)
    LORD_OF_WAR = ("Lord of War", "Lord of War",)
    TROOPS = ("Troops", "Troops",)


class BattlefieldRole(Model):
    title = CharField(_("title"), db_index=True, max_length=19, unique=True)

    class Meta:
        constraints = (
            CheckConstraint(check=Q(title__in=Title.values), name="%(app_label)s_%(class)s_title_valid"),
        )
        verbose_name = _("battlefield role")
        verbose_name_plural = _('battlefield roles')

    def __str__(self):
        return self.title
