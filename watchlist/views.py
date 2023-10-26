from rest_framework.response import Response
from rest_framework import status
from watchlist.models import Movie
from watchlist.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    """
    Retrieve a list of movies.

    This view retrieves a list of all movies from the database and serializes them using MovieSerializer.

    Args:
        request: HTTP request object.

    Returns:
        Response: Serialized movie data as a JSON response or an error response in case of an exception.
    """
    try:
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        error_message = "An error occurred while retrieving movie data."
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def movie_details(request,pk):
    """
    Retrieve details of a specific movie.

    This view retrieves details of a movie with the specified primary key (pk) from the database and serializes it using MovieSerializer.

    Args:
        request: HTTP request object.
        pk: Primary key of the movie to retrieve.

    Returns:
        Response: Serialized movie data as a JSON response or an error response in case of an exception.
    """
    try:
        queryset = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        error_message = "An error occurred while retrieving movie details."
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)