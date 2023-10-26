from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text="Unique identifier for the movie")
    name = serializers.CharField(max_length=255, help_text="Name of the movie")
    description = serializers.CharField(help_text="Description of the movie")
    active = serializers.BooleanField(help_text="Is the movie currently active")
