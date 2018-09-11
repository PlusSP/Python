from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class News(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
        null=False,
        blank=False,
        validators=[MinLengthValidator(3)]
    )
    preview = models.CharField(
        verbose_name='Анонс',
        max_length=150,
        null=False,
        blank=False,
    )
    text = models.TextField(
        verbose_name='Текст',
        null=False,
        blank=False,
        validators=[MinLengthValidator(10)]
    )
    image = models.ImageField(
        upload_to='Music_Blog/images/',
        null=True,
        blank=True,
    )
    post_date = models.DateTimeField(

        auto_now_add=True
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Album(models.Model):
    title = models.CharField(
        verbose_name='Название альбома',
        max_length=255,
    )
    year = models.CharField(
        verbose_name='Год',
        max_length=4,
    )
    genre = models.ForeignKey(
        to='Genre',
        related_name='album',
        on_delete=models.SET_NULL,
        null=True
    )
    album_art = models.ImageField(
        upload_to='Music_Blog/album_art/',
        null=True,
        blank=True
    )
    artist = models.ForeignKey(
        to='Artist',
        related_name='albums',
        on_delete=models.SET_NULL,
        null=True
    )
    tracklist = models.TextField(
        verbose_name='tracklist',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.title}'


class Artist(models.Model):
    name = models.CharField(
        verbose_name='Исполнитель',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'
