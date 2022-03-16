from rest_framework import serializers
from movie.models import Director, Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    # movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title director reviews reviews_count rating_average'.split()

    def get_reviews(self, movie):
        # filtered_review = Review.objects.filter(movie=movie, stars__gte=4)
        filtered_review = movie.reviews.filter(stars__gte=4)
        return ReviewSerializer(filtered_review, many=True).data


    def get_reviews_count(self, movie):
        return movie.reviews.filter(stars__gte=4).count()

class MovieRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title rating_average'.split()




