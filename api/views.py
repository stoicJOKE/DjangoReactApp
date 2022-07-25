from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Musician, Album
from .serializers import MusicianSerializer, AlbumSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/musicians',
        'GET /api/musician/:id',
        'GET /api/album',
    ]
    return Response(routes)


@api_view(['GET'])
def getMusicians(request):
    musician = Musician.objects.all()
    serializer = MusicianSerializer(musician, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMusician(request, pk):
    musician = Musician.objects.get(id=pk)
    serializer = MusicianSerializer(musician, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAlbum(request):
    album = Album.objects.all()
    serializer = AlbumSerializer(album, many=True)
    return Response(serializer.data)
