from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie.serializers import DirectorSerializer
from movie.models import Director

from movie.serializers import MovieSerializer, MovieRateSerializer
from movie.models import Movie

from movie.serializers import ReviewSerializer
from movie.models import Review

@api_view(['GET'])
def director_list_view(request):
    movie = Director.objects.all()
    serializer = DirectorSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_list_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_list_view(request):
    movie = Review.objects.all()
    serializer = ReviewSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        movie = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_item_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_rating_view(request):
    movie = Movie.objects.all()
    serializer = MovieRateSerializer(movie, many=False)
    return Response(data=serializer.data)



