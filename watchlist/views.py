from rest_framework import status 
from watchlist.models import WatchList, StreamPlatform
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from watchlist.serializers import WatchListSerializer, StreamPlatformSerializer

class WatchListView(APIView):
    """
    View for listing and creating movies.

    This view supports both retrieving a list of all movies and creating a new movie entry.

    Attributes:
        serializer_class: The serializer class for Movie objects.
    """
    serializer_class = WatchListSerializer

    def get(self, request):
        """
        Retrieve a list of movies.

        Args:
            request: HTTP request object.

        Returns:
            Response: Serialized movie data as a JSON response.
        """
        queryset = WatchList.objects.all()
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
    serializer_class = WatchListSerializer

    def get(self, request, pk):
        """
        Retrieve details of a specific movie.

        Args:
            request: HTTP request object.
            pk: Primary key of the movie to retrieve.

        Returns:
            Response: Serialized movie data as a JSON response or an error response in case of a not found exception.
        """
        movie = get_object_or_404(WatchList, pk=pk)
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
        movie = get_object_or_404(WatchList, pk=pk)
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
        movie = get_object_or_404(WatchList, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)       
    
class StreamPlatformListView(APIView):
    """
    API endpoint for listing and creating stream platforms.

    GET:
    Retrieve a list of all stream platforms.

    POST:
    Create a new stream platform.
    """
    serializer_class = StreamPlatformSerializer

    def get(self, request):
        """
        Retrieve a list of all stream platforms.

        Returns:
            Response: A JSON response containing a list of stream platforms.
        """
        queryset = StreamPlatform.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new stream platform.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response with the created stream platform or validation errors.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailView(APIView):
    """
    API endpoint for retrieving, updating, and deleting a specific stream platform.

    GET:
    Retrieve a specific stream platform.

    PUT:
    Update a specific stream platform.

    DELETE:
    Delete a specific stream platform.
    """
    serializer_class = StreamPlatformSerializer

    def get(self, request, pk):
        """
        Retrieve a specific stream platform.

        Args:
            request: The HTTP request object.
            pk: The primary key of the stream platform.

        Returns:
            Response: A JSON response containing the stream platform details.
        """
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = self.serializer_class(platform)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Update a specific stream platform.

        Args:
            request: The HTTP request object.
            pk: The primary key of the stream platform.

        Returns:
            Response: A JSON response with the updated stream platform or validation errors.
        """
        platform = get_object_or_404(StreamPlatform, pk=pk)
        serializer = self.serializer_class(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific stream platform.

        Args:
            request: The HTTP request object.
            pk: The primary key of the stream platform.

        Returns:
            Response: An empty JSON response with a 204 No Content status.
        """
        platform = get_object_or_404(StreamPlatform, pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)