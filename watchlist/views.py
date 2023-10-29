from rest_framework import status 
from watchlist.models import Movie
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from watchlist.serializers import MovieSerializer

class MovieListView(APIView):
    """
    View for listing and creating movies.

    This view supports both retrieving a list of all movies and creating a new movie entry.

    Attributes:
        serializer_class: The serializer class for Movie objects.
    """
    serializer_class = MovieSerializer

    def get(self, request):
        """
        Retrieve a list of movies.

        Args:
            request: HTTP request object.

        Returns:
            Response: Serialized movie data as a JSON response.
        """
        queryset = Movie.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new movie entry.

        Args:
            request: HTTP request object.

        Returns:
            Response: Serialized movie data as a JSON response or an error response in case of validation failure.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MovieDetailView(APIView):
    """
    View for retrieving, updating, or deleting a movie.

    This view supports retrieving details, updating, and deleting a specific movie.

    Attributes:
        serializer_class: The serializer class for Movie objects.
    """
    serializer_class = MovieSerializer

    def get(self, request, pk):
        """
        Retrieve details of a specific movie.

        Args:
            request: HTTP request object.
            pk: Primary key of the movie to retrieve.

        Returns:
            Response: Serialized movie data as a JSON response or an error response in case of a not found exception.
        """
        movie = get_object_or_404(Movie, pk=pk)
        serializer = self.serializer_class(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update details of a specific movie.

        Args:
            request: HTTP request object.
            pk: Primary key of the movie to update.

        Returns:
            Response: Serialized movie data as a JSON response after update or an error response in case of validation failure.
        """
        movie = get_object_or_404(Movie, pk=pk)
        serializer = self.serializer_class(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific movie.

        Args:
            request: HTTP request object.
            pk: Primary key of the movie to delete.

        Returns:
            Response: A success response indicating the movie has been deleted.
        """
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       