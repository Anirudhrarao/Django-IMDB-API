from django.urls import path
from watchlist.views import WatchListView, MovieDetailView,StreamPlatformListView, StreamPlatformDetailView

urlpatterns = [
    path('', WatchListView.as_view(), name = 'watch-list'),    
    path('<int:pk>/', MovieDetailView.as_view(), name = 'movie-detail'),    
    path('platform/', StreamPlatformListView.as_view(), name = 'platform-list'),    
    path('platform/<int:pk>/', StreamPlatformDetailView.as_view(), name = 'platform-detail'),    
]



