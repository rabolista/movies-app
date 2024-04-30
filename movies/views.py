from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies' : ['Avengers End Game', 'IronMan', 'Titanic']

    }
    return render(request, 'movies/index.html', {'movies' : context['movies']})

def about(request):
    return render(request, 'movies/about.html', {})