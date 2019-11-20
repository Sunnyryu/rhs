from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.
def movie(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie.html', {'movies': movies})
def new(request):
    if request.method == "POST":
        title=request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        post = request.POST.get('post')
        description = request.POST.get('description')
        movie = Movie()
        movie.title = title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.post = post
        movie.description = description
        movie.save()
        return redirect('movie:movie')
    else:
        return render(request, 'movie/new.html')
def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
            'movie':movie
            }
    return render(request, 'movie/detail.html', context)
def edit(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == "POST":
        title=request.POST.get('title')
        title_en = request.POST.get('title_en')
        audience = request.POST.get('audience')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        watch_grade = request.POST.get('watch_grade')
        score = request.POST.get('score')
        post = request.POST.get('post')
        description = request.POST.get('description')
        movie = Movie()
        movie.title = title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.post = post
        movie.description = description
        movie.save()
        return redirect('movie:detail', movie_id)
    else:
        context = { 'movie':movie }
        return render(request, 'movie/edit.html', context)
def delete(request, movie_id):
    if request.method == "POST":
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('movie:movie')
    else:
        return redirect('movie:detail', movie_id)
