"""Models for the ``entry_attachments`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EntryAttachment(models.Model):
    """
    Mapping class to map ``Entry`` objects to ``Document`` objects.

    """
    entry = models.ForeignKey(
        'cmsplugin_blog.Entry',
        verbose_name=_('Entry'),
        related_name='attachments',
    )

    document = models.ForeignKey(
        'document_library.Document',
        verbose_name=_('Document'),
        related_name='attachments',
    )

    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        null=True, blank=True,
    )

    class Meta:
        ordering = ['position', ]
