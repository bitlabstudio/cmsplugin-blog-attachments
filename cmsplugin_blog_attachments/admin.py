"""Admin classes for the ``entry_attachments`` app."""
from django.contrib import admin

from cmsplugin_blog.admin import EntryAdmin

from .models import EntryAttachment


class EntryAttachmentInline(admin.TabularInline):
    model = EntryAttachment
    extra = 1
    raw_id_fields = ['document', ]


EntryAdmin.inlines = EntryAdmin.inlines[:] + [EntryAttachmentInline]
