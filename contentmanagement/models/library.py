from django.db import models

from contentmanagement.models import TimeModel


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

    description = models.TextField()

    type = models.CharField(
        choices=TYPES,
        default=TYPE_BOOK,
        max_length=50,
        verbose_name='تایپ'
    )

    user = models.ForeignKey(
        'contentmanagement.User',
        on_delete=models.CASCADE,
        related_name='libraries',
        verbose_name='کاربر'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'کتاب‌خانه'
        verbose_name_plural = "کتاب‌خانه‌ها"
        unique_together = ('user', 'name')
