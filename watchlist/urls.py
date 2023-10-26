from django.urls import path
from watchlist.views import movie_list, movie_details

urlpatterns = [
    path('', movie_list, name = 'watch-list'),    
    path('details/<int:pk>', movie_details, name = 'movie-detail'),    
]



