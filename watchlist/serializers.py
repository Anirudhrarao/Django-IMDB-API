from rest_framework import serializers
from watchlist.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = WatchList
        fields = "__all__"
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist is name which is given in foreign key as related name
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"        


        