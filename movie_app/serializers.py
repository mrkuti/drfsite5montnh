from movie_app.models import Director, Review, Movie
from rest_framework import serializers





class DirectorSerializer(serializers.ModelSerializer):
    # title = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie_id'.split()




class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'title description duration director_id reviews rating'.split()




class DirectorValidateSerializers(serializers.Serializer):
    name = serializers.CharField(min_length=5, max_length=500)



class MovieValidateSerializers(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=500)
    description = serializers.CharField(min_length=5, max_length=500)
    duration = serializers.IntegerField(min_value=50, max_value=500)


class ReviesValidateSerializers(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=1000)
    stars = serializers.IntegerField(min_value=1, max_value=5)