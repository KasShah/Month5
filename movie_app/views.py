from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET', 'PUT'])
def directors_api_view(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def directors_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = get_object_or_404(Director, id=id)
        serializer = DirectorSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def movies_api_view(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def movies_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = get_object_or_404(Director, id=id)
        serializer = MovieSerializer(queryset, many=False)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def reviews_api_view(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = get_object_or_404(Director, id=id)
        serializer = ReviewSerializer(queryset, many=False)
        return Response(serializer.data, status=200)
