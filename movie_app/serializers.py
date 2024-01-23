from rest_framework import serializers
from .models import Director, Movie, Review

def validate_name_min_lenght(value, min_lenght):
    if len(value) < min_lenght:
        raise serializers.ValidationError(f'Минимальная длина для этого поля {min_lenght}')


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movie_count(self, obj):
        return obj.movies.count()
    def validate_name(self, value):
        validate_name_min_lenght(value, 7)
        return value


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if num_reviews > 0:
            return total_stars / num_reviews
        return 0.0

    def validate_title(self, value):
        validate_name_min_lenght(value, 3)
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_min_lenght(value, 10)
        return value
