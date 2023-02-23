from django.db import models

from contentmanagement.models import TimeModel

ATTACHMENTS = {'video': {'subtitle': '.srt'}, 'picture': {'caption': '.txt'}, 'music': {'lyrics': '.txt'},
               'book': {'audio': '.mp3'}}


class Library(TimeModel):
    TYPE_BOOK = 'book'
    TYPE_VIDEO = 'video'
    TYPE_MUSIC = 'music'
    TYPE_PICTURE = 'picture'

    TYPES = (
        (TYPE_BOOK, "کتاب"),
        (TYPE_VIDEO, "ویدئو"),
        (TYPE_MUSIC, "موزیک"),
        (TYPE_PICTURE, 'عکس'),
    )

    name = models.CharField(
        max_length=60,
        verbose_name='نام'
    )

    description = models.TextField(null=True, blank=True)

    file_attributes = models.TextField(null=True, blank=True)

    type = models.CharField(
        choices=TYPES,
        default=TYPE_BOOK,
        max_length=50,
        verbose_name='تایپ'
    )

    owner = models.ForeignKey(
        'contentmanagement.User',
        on_delete=models.DO_NOTHING,
        related_name='owned_libraries',
        verbose_name='صاحب'
    )

    users = models.ManyToManyField(
        to='contentmanagement.User',
        related_name='libraries',
        blank=True,
        null=True,
        verbose_name='کاربر‌ها'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'کتاب‌خانه'
        verbose_name_plural = "کتاب‌خانه‌ها"
        unique_together = ('owner', 'name', 'type')
