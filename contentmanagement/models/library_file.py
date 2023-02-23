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

    description = models.TextField()

    def __str__(self):
        return self.file.name

    def file_name(self):
        return os.path.basename(self.file.name)
