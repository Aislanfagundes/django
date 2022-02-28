from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': "682825940"},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': "682827736"},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
