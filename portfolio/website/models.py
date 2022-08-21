from django.db import models
from portfolio.settings import MEDIA_URL, MEDIA_ROOT


class Project(models.Model):
    title = models.CharField(
        default='default title',
        verbose_name='Заголовок',
        max_length=20
    )
    short_description = models.TextField(
        default='default description',
        verbose_name='Описание'
    )
    technology = models.CharField(
        max_length=20,
        verbose_name='Технологии',
        blank=True
    )
    link = models.CharField(
        max_length=150,
        verbose_name='Ссылка',
        blank=True
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение'
    )
    def __str__(self):
        return self.title
