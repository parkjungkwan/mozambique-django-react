from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from multiplex.movies.repository import MovieRepository
from multiplex.movies.serializers import MovieSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def create_movie(request): return MovieSerializer().create(request.data)

@api_view(['PUT'])
@parser_classes([JSONParser])
def update_movie(request): return MovieSerializer().update(request.data)

@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_movie(request): return MovieSerializer().delete(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def movie_list(request): return MovieRepository().get_all(request.data)

@api_view(['GET'])
@parser_classes([JSONParser])
def find_movie_by_id(request): return MovieRepository().find_by_id(request.data)

