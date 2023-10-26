from django.shortcuts import render
from watchlist.models import Movie
from django.http import JsonResponse, HttpResponse

def movie_list(request):
    queryset = Movie.objects.all()
    movie_list = {
        'data': list(queryset.values())
    }
    return JsonResponse(movie_list)

def movie_details(request,pk):
    queryset = Movie.objects.get(pk=pk)
    movie_data = {
        'Id': queryset.id,
        'Name': queryset.name,
        'Description': queryset.description,
        'Active': queryset.active
    }    
    return JsonResponse(movie_data)