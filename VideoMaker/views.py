from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import VideoMaker, Duration
from .serializers import VideoMakerSerializer


from rest_framework.response import Response
from rest_framework import status


class AudioCreateApiView(generics.CreateAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer



class AudioListApiView(generics.RetrieveAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
    lookup_field = 'pk'


class AudioUpdateApiView(generics.UpdateAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
    lookup_field = 'pk'


class AudioDeleteApiView(generics.DestroyAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
    lookup_field = 'pk'    
    
    def perform_destroy(self,instance):
        super().perform_destroy(instance)


class AudioListView(generics.ListAPIView):
    queryset = VideoMaker.objects.all()
    serializer_class = VideoMakerSerializer
