from django.contrib import admin

from Music_Blog import models

admin.site.register(
    models.News
)

admin.site.register(
    models.Album
)

admin.site.register(
    models.Artist
)

admin.site.register(
    models.Genre
)
