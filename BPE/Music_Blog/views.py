from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from .models import News, Artist, Album, Genre


def index(request):
    return render(request, 'index.html', {
            'news': News.objects.all().order_by('-post_date')
        })


def artists(request):
    # artist_list = Artist.objects.all().order_by('name').prefetch_related('albums')
    return render(request, 'artists.html', {
        'artists': Artist.objects.all().order_by('name'),
        'albums': Album.objects.all().order_by('artist__name')
    })


def albums(request):
    return render(request, 'albums.html', {
        'albums': Album.objects.all().order_by('title'),
    })


def genres(request):
    return render(request, 'genres.html', {
        'genres': Genre.objects.all().order_by('name'),
        # 'albums': Album.objects.all().order_by('genre__name')
    })


def detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    text = mark_safe(news.text)
    return render(request, 'detail.html', {
            'news': news,
            'text': text
        })


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tracklist = mark_safe(album.tracklist)
    return render(request, 'album_detail.html', {
            'album': album,
            'tracklist': tracklist
        })


def artist_detail(request, pk):
    albums = Album.objects.filter(artist__id=pk)
    artist = Artist.objects.get(id=pk)
    return render(request, 'artist_detail.html', {
            'albums': albums,
            'artist': artist
        })


def genre_detail(request, pk):
    albums = Album.objects.filter(genre__id=pk)
    genre = Genre.objects.get(id=pk)
    return render(request, 'genre_detail.html', {
            'albums': albums,
            'genre': genre
        })


def vintage(request):
    return render(request, 'zVintauge/index.html')


def archive(request):
    return render(request, 'zVintauge/archive.html')


def contact(request):
    return render(request, 'zVintauge/contact.html')


def gallery(request):
    return render(request, 'zVintauge/gallery.html')


def single(request):
    return render(request, 'zVintauge/single.html')


