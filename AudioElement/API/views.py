from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from VideoMaker.models import VideoMaker

@api_view()
def api_response(request,*args,**kwargs):
    """
    MAIN API VIEW
    """
    # need serializer