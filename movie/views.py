from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie.serializers import DirectorSerializer
from movie.models import Director

from movie.serializers import MovieSerializer, MovieRateSerializer
from movie.models import Movie

from movie.serializers import ReviewSerializer
from movie.models import Review

@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        movie = Director.objects.all()
        serializer = DirectorSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        name_cr = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(name_cr).data)

@api_view(['GET','POST'])
def movie_list_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director')
        movie_cr = Movie.objects.create(title=title, description=description,
                                        duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movie_cr).data)

@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        movie = Review.objects.all()
        serializer = ReviewSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie')
        review_cr = Review.objects.create(text=text, movie=movie_id)
        return Response(data=ReviewSerializer(review_cr).data)



@api_view(['GET', 'PUT', 'DELETE'])
def director_item_view(request, id):
    try:
        movie = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Director deleted'})
    else:
        movie.name = request.data.get('name')
        movie.save()
        return Response(data=DirectorSerializer(movie).data)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Movie deleted'})
    else:
        movie.title = request.data.get('title')
        movie.duration = request.data.get('duration')
        movie.description = request.data.get('description')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return  Response(data=MovieSerializer(movie).data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_item_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Not found!!!!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Review deleted'})
    else:
        movie.text = request.data.get('text')
        movie.movie_id = request.data.get('movie')
        movie.save()
        return Response(data=ReviewSerializer(movie).data)

@api_view(['GET'])
def movie_rating_view(request):
    movie = Movie.objects.all()
    serializer = MovieRateSerializer(movie, many=False)
    return Response(data=serializer.data)



