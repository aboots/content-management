from uuid import uuid4

from django.contrib.auth.hashers import make_password
from django.db import models

from .time_model import TimeModel


class User(TimeModel):
    username = models.CharField(
        max_length=80,
        unique=True,
        verbose_name='یوزرنیم'
    )

    first_name = models.CharField(
        max_length=60,
        verbose_name='نام'
    )

    last_name = models.CharField(
        max_length=60,
        verbose_name='نام خانوادگی'
    )

    password = models.CharField(
        max_length=200,
        verbose_name='پسورد'
    )

    email = models.EmailField(
        verbose_name='ایمیل'
    )

    token = models.CharField(
        null=True,
        blank=True,
        max_length=40,
        verbose_name='توکن'
    )

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_token()
            self.password = make_password(self.password)
        else:
            user = User.objects.filter(pk=self.id).first()
            if user.password != self.password:
                self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def set_token(self):
        self.token = str(uuid4())

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = "کاربر ها"
