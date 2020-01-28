from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Anuj C.',
        'title': 'Blog-Post',
        'content': 'First post content',
        'date_posted': 'August 28 2020'
    },
    {
        'author': 'New Me',
        'title': 'Blog-Post',
        'content': 'First post content',
        'date_posted': 'August 28 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
