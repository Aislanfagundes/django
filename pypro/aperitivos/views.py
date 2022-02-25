from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': "681076510?h=af518b33fe"}
    return render(request, 'aperitivos/video.html', context={'video': video})
