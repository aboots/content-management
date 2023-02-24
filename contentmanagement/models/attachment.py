import os

from django.db import models

from contentmanagement.models import TimeModel


class Attachment(TimeModel):
    field = models.CharField(max_length=60)

    library_file = models.ForeignKey(
        'contentmanagement.LibraryFile',
        related_name='attachments',
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='library/files/'
    )

    def file_name(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'پیوست'
        verbose_name_plural = 'پیوست ها'
        unique_together = ('library_file', 'file')
