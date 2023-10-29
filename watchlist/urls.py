from django.urls import path
from watchlist.views import MovieListView, MovieDetailView

urlpatterns = [
    path('', MovieListView.as_view(), name = 'watch-list'),    
    path('details/<int:pk>', MovieDetailView.as_view(), name = 'movie-detail'),    
]



