from django.db.models import CharField, Model, TextField
from django.utils.translation import gettext_lazy as _


class Ability(Model):
    description = TextField(_("description"), max_length=255)
    title = CharField(_("title"), db_index=True, max_length=25, unique=True)

    class Meta:
        verbose_name = _("ability")
        verbose_name_plural = _("abilities")

    def __str__(self):
        return self.title
