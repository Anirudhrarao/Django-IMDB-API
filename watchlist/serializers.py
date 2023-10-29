from rest_framework import serializers
from watchlist.models import Movie
from watchlist.validators import is_capitalized

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text="Unique identifier for the movie")
    name = serializers.CharField(max_length=255, help_text="Name of the movie", validators=[is_capitalized])
    description = serializers.CharField(help_text="Description of the movie")
    active = serializers.BooleanField(help_text="Is the movie currently active")

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    # object-level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("The name and description should not be the same.")
        return data

    
    # Field-level validation 
    def validate_name(self, value):
        if len(value) <= 3:
            raise serializers.ValidationError("The name must be longer than 3 characters.")        
        return value
