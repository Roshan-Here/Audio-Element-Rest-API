from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import VideoMaker, Duration
from .serializers import VideoMakerSerializer


from rest_framework.response import Response
from rest_framework import status


class AudioCreateApiView(generics.ListCreateAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer

    def perform_create(self, validated_data):
        datas = validated_data.pop('duration')
        duration_data = VideoMaker.objects.create(**validated_data)
        for audio in datas:
            Duration.objects.create(duration=duration_data,**datas)
        return duration_data


    # def create(self, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     musician = Musician.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         Album.objects.create(artist=musician, **album_data)
    #     return musician

    #     nice = duration_data.get('end_time')
    #     stime = duration_data.get('start_time')
    #     print(duration_data)
    #     print(nice,stime)
    #     wow = Duration.objects.set(end_time=nice,start_time=stime)
    #     wow.save()

    #     vidmaker = VideoMaker.objects.create(duration=wow,**serializer.validated_data)
    #     return vidmaker
        # super().perform_create(serializer)



class AudioListApiView(generics.RetrieveAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
    lookup_field = 'pk'