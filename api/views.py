from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from django.http import Http404

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


# @api_view(['GET', 'POST'])
# def getMusicians(request):
#     if request.method == 'GET':
#         musician = Musician.objects.all()
#         serializer = MusicianSerializer(musician, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         reqdata = MusicianSerializer(data=request.data)
#         if reqdata.is_valid():
#             reqdata.save()
#             return Response(reqdata.data, status=status.HTTP_201_CREATED)
#         return Response(reqdata.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def getMusician(request, pk):
#     musician = Musician.objects.get(id=pk)
#     serializer = MusicianSerializer(musician, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getAlbum(request):
#     album = Album.objects.all()
#     serializer = AlbumSerializer(album, many=True)
#     return Response(serializer.data)


# class based views

# class StudioList(APIView):
#     def get(self, request, format=None):
#         musician = Musician.objects.all()
#         serializer = MusicianSerializer(musician, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         reqdata = MusicianSerializer(data=request.data)
#         if reqdata.is_valid():
#             reqdata.save()
#             return Response(reqdata.data, status=status.HTTP_201_CREATED)
#         return Response(reqdata.errors, status=status.HTTP_400_BAD_REQUEST)


# using mixins and generic class


# class StudioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Musician.objects.all()
#     serializer_class = MusicianSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# using Generic based class views

class StudioList(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
