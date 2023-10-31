from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = WatchList
        fields = "__all__"
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist is name which is given in foreign key as related name
    watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-detail")
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"        


        