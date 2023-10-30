from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    length_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
    
    # custom fields of serializer
    def get_length_name(self,object):
        return len(object.name)
    
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description of movie should not be the same.")
        return data

    
