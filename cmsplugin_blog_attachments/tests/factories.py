"""Factories for the ``cmsplugin_blog_attachments`` app."""
import factory

from document_library.tests.factories import DocumentFactory
from cmsplugin_blog.models import Entry

from ..models import EntryAttachment


class EntryFactory(factory.Factory):
    """Factory for the ``Entry`` model."""
    FACTORY_FOR = Entry


class EntryAttachmentFactory(factory.Factory):
    """Factory for the ``EntryAttachment`` model."""
    FACTORY_FOR = EntryAttachment

    entry = factory.SubFactory(EntryFactory)
    document = factory.SubFactory(DocumentFactory)
