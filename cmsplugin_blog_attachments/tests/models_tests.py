"""Tests for the models of the ``cmsplugin_blog_attachments`` app."""
from django.test import TestCase

from .factories import EntryAttachmentFactory


class EntryAttachmentTestCase(TestCase):
    """Tests for the ``EntryAttachment`` model."""
    longMessage = True

    def test_model(self):
        obj = EntryAttachmentFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
