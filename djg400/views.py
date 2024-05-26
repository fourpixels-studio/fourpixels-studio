from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Track
from seo_management.models import SEO
from django.http import JsonResponse


def mixes_list(request):
    context = {
        'title_tag': "DJ G400 Mixes",
        'meta_description': "DJ G400 Mixes",
        'meta_keywords': "DJ G400 Mixes",
        'meta_thumbnail': SEO.objects.get(pk=1).meta_thumbnail.url,
    }
    return render(request, 'mixes_list.html', context)


def remixes_list(request):
    context = {
        'title_tag': "DJ G400 Remixes",
        'meta_description': "DJ G400 Remixes",
        'meta_keywords': "DJ G400 Remixes",
        'meta_thumbnail': SEO.objects.get(pk=1).meta_thumbnail.url,
        'tracks': Track.objects.all(),
    }
    return render(request, 'remixes_list.html', context)


def remix_detail(request, slug):
    track = get_object_or_404(Track, slug=slug)
    context = {
        'title_tag': "DJ G400 Remixes",
        'meta_description': "DJ G400 Remixes",
        'meta_keywords': "DJ G400 Remixes",
        'meta_thumbnail': SEO.objects.get(pk=1).meta_thumbnail.url,
        'track': track,
    }
    return render(request, 'remix_detail.html', context)


def update_download_count(request, track_id):
    if request.method == 'POST':
        track = get_object_or_404(Track, id=track_id)
        track.download_count += 1
        track.save()
        return JsonResponse({'status': 'success', 'download_count': track.download_count})
    return JsonResponse({'status': 'fail'}, status=400)
