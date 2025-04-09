from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .models import Film
from .serializers import FilmSerializer, FilmDetailSerializer


@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Film does not exist!'})
    data = FilmDetailSerializer(film).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def film_list_api_view(request):
    # step 1: Collect films from DB (QuerySet)
    films = Film.objects.all()

    # step 2: Reformat (Serialize) films to List of dictionary
    data = FilmSerializer(films, many=True).data

    # step 3: Return Response with data and status
    return Response(data=data,
                    status=status.HTTP_200_OK)
