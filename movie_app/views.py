from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def directors_api_view(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_api_view(request, id):
    queryset = get_object_or_404(Director, id=id)
    if request.method == 'GET':
        serializer = DirectorSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)



@api_view(['GET', 'POST'])
def movies_api_view(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_api_view(request, id):
    queryset = get_object_or_404(Director, id=id)
    if request.method == 'GET':
        serializer = MovieSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = MovieSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def reviews_api_view(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    queryset = get_object_or_404(Director, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)
