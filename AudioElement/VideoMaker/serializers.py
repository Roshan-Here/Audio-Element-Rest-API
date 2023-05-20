from rest_framework import serializers

from .models import VideoMaker

class VideoMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaker
        fields = [
            'typee',
            'high_volume',
            'low_volume',
            'video_component_id',
            'url',
            'start_time',
            'end_time',
        ]