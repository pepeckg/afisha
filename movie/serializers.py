from rest_framework import serializers
from .models import Director, Movie, Review, Tag




class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title description duration director reviews'.split()


class DirectorSerializer(serializers.ModelSerializer):
    movie_type = MovieSerializer(many=True, read_only=True)
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movie_count movie_type'.split()

    def get_movie_count(self, director):
        return director.movie_type.count()



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('movie', 'text', 'stars')




class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    class Meta:
        model = Movie
        fields = ('title', 'reviews', 'average_rating')
class TagValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')






