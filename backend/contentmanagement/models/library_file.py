import os

from django.db import models

from contentmanagement.models import TimeModel


class LibraryFile(TimeModel):
    library = models.ForeignKey(
        'contentmanagement.Library',
        related_name='files',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='library/files/'
    )

    description = models.TextField(null=True, blank=True)

    attributes = models.JSONField(null=True, blank=True)

    attachment_fields = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.file.name

    def file_name(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل ها'
        unique_together = ('library', 'file')
