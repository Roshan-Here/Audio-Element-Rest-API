from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import VideoMaker
from .serializers import VideoMakerSerializer


from rest_framework.response import Response


class AudioCreateApiView(generics.CreateAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer

    def perform_create(self, serializer):
        duration_data = serializer.validated_data
        print(duration_data)
        return Response(status=201)
    #     duration_data = serializer.validated_data.pop('duration')
    #     print(duration_data)
    #     # print(duration_data.get('start_time'))
    #     vidmaker = VideoMaker.objects.create(**serializer.validated_data)
    #     starttime = duration_data.get('start_time')
    #     endtime = duration_data.get('end_time')
    #     print(starttime,endtime)
    #     print(serializer.validated_data)
        # VideoMakerSerializer.objects.create(start_time=starttime, end_time=endtime,**duration_data)
        # print(VideoMaker.objects.all)
        # return vidmaker


    # def perform_save(self,serializer):
    #     start_time = serializer.validated_data.get('start_time')
    #     end_time = serializer.validated_data.get('end_time')
    #     serializer.save(start_time=start_time,end_time=end_time)


class AudioListApiView(generics.ListAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
