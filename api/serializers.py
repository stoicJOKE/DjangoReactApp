from rest_framework.serializers import ModelSerializer
from app.models import Musician, Album


class MusicianSerializer(ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
