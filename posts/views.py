from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Monicaco',
        'user': {
            'name': 'Gonzalo M',
            'picture': 'https://static.platzi.com/media/avatars/avatars/gonzaloan_09fb848a-ab43-476f-943b-de151d3f0a4e.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://d3f4nerl4dh38d.cloudfront.net/sites/elnaveghable.cl/files/imagecache/380x285/imagen_noticia/mono_vio_truco_de_magia.jpg'
    },
    {
        'title': 'Pork',
        'user': {
            'name': 'Chancho D',
            'picture': 'https://static.platzi.com/media/avatars/avatars/gonzaloan_09fb848a-ab43-476f-943b-de151d3f0a4e.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjANNqQg3ajpdmpLMINGOKP-KLqCBDbWMnUq5oxXx7QJn2-LCp'
    },
    {
        'title': 'Monochico',
        'user': {
            'name': 'Monicake M',
            'picture': 'https://static.platzi.com/media/avatars/avatars/gonzaloan_09fb848a-ab43-476f-943b-de151d3f0a4e.jpg'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgvsxvj44EtBK2wCzy8w_n6kbBO6Ucgs1vckZMxb9LtUb0Q-Q6'
    }
]


def list_posts(request):
    # List existing posts
    return render(request, 'feed.html', {'posts': posts})

# Create your views here.
