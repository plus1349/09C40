from django.conf import settings
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _


class BattlefieldRoleTranslation(Model):
    battlefield_role = ForeignKey(
        "roles.BattlefieldRole", on_delete=CASCADE, related_name="translations", verbose_name=_('battlefield role')
    )
    locale = CharField(_("locale"), choices=settings.LANGUAGES[1:], max_length=2)
    title = CharField(_("title"), db_index=True, max_length=25, unique=True)

    class Meta:
        unique_together = ("battlefield_role", "locale")
        verbose_name = _("battlefield role translation")
        verbose_name_plural = _("battlefield role translations")

    def __str__(self):
        return self.title
