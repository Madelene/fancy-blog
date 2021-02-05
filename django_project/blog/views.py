from django.shortcuts import render

posts = [
    {
        'author': 'Maddie',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 5, 2021'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 6, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
