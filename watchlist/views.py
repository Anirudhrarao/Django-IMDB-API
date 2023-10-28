from rest_framework.response import Response
from rest_framework import status
from watchlist.models import Movie
from watchlist.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def movie_list(request):
    """
    Retrieve a list of movies or create a new movie entry.

    This view supports both retrieving a list of all movies and creating a new movie entry. GET requests retrieve movie data, while POST requests create a new movie entry.

    Args:
        request: HTTP request object.

    Returns:
        Response: Serialized movie data as a JSON response for GET requests or a success response for POST requests. In case of an exception, it returns an error response.

    Raises:
        Exception: If there is an error during the process.
    """
    if request.method == 'GET':
        try:
            queryset = Movie.objects.all()
            serializer = MovieSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = "An error occurred while retrieving movie data."
            return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, pk):
    """
    Retrieve details of a specific movie, update, or delete it.

    This view retrieves details of a movie with the specified primary key (pk) from the database and serializes it using MovieSerializer. It also supports updating or deleting the movie.

    Args:
        request: HTTP request object.
        pk: Primary key of the movie to retrieve, update, or delete.

    Returns:
        Response: Serialized movie data as a JSON response for GET requests, or a success response for PUT requests, or a success response for DELETE requests. In case of an exception, it returns an error response.

    Raises:
        Exception: If there is an error during the process.
    """
    try:
        movie = Movie.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        if request.method == 'PUT':
            serializer = MovieSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        error_message = "An error occurred while processing the movie request."
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)