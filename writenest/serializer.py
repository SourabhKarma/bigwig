from .models import *
from rest_framework import serializers, fields






# class AlbumSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Album
#         fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


# class MusicianSerializer(serializers.ModelSerializer):

#     album_musician = AlbumSerializer(many=True)

#     class Meta:
#         model = Musician
#         fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

#     def create(self, validated_data):
#         albums_data = validated_data.pop('album_musician')
#         musician = Musician.objects.create(**validated_data)
#         for album_data in albums_data:
#             Album.objects.create(artist=musician, **album_data)
#         return musician

#     def update(self, instance, validated_data):
#         albums_data = validated_data.pop('album_musician')
#         albums = (instance.album_musician).all()
#         albums = list(albums)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.instrument = validated_data.get('instrument', instance.instrument)
#         instance.save()

#         for album_data in albums_data:
#             album = albums.pop(0)
#             album.name = album_data.get('name', album.name)
#             album.release_date = album_data.get('release_date', album.release_date)
#             album.num_stars = album_data.get('num_stars', album.num_stars)
#             album.save()
#         return instance







#  2



class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryName1
        fields = ['name']




class TeslaModelSerializer(serializers.ModelSerializer):
    origin = CountryNameSerializer(many=True)

    class Meta:
        model = TeslaModel1
        fields = ['model_name', 'price', 'origin']

    def create(self, validated_data):
        origin_data = validated_data.pop('origin')
        tesla = TeslaModel1.objects.create(**validated_data)
        for data in origin_data:
            CountryName1.objects.create(**data)
        return tesla



