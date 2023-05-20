from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from VideoMaker.models import VideoMaker

from VideoMaker.serializers import VideoMakerSerializer
@api_view()
def api_response(request,*args,**kwargs):
    """
    MAIN API VIEW
    """
    # need serializer
    serializer = VideoMakerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({'Errr invalid': 'not required data'},status=404)