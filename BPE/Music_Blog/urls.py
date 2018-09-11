from django.urls import path

from Music_Blog import models, views

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.albums, name='albums'),
    path('artists', views.artists, name='artists'),
    path('genres', views.genres, name='genres'),
    path('<int:pk>', views.detail, name='detail'),
    path('albums<int:pk>', views.album_detail, name='album_detail'),
    path('artist<int:pk>', views.artist_detail, name='artist_detail'),
    path('genre<int:pk>', views.genre_detail, name='genre_detail'),
    path('vintage', views.vintage, name='vintage'),
    path('archive', views.archive, name='archive'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('single', views.single, name='single'),
]