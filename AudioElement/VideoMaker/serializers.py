from rest_framework import serializers

from .models import VideoMaker,Duration

class DuratinSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = (
            'start_time',
            'end_time',
        )


class VideoMakerSerializer(serializers.ModelSerializer):
    duration = DuratinSeriaizer()
    class Meta:
        model = VideoMaker
        fields = (
            'typee',
            'high_volume',
            'low_volume',
            'video_component_id',
            'url',
            'duration',
        )
