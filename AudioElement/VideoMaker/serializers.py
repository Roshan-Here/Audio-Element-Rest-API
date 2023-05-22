from rest_framework import serializers

from .models import VideoMaker,Duration

class DuratinSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Duration
        fields = [
            'id',
            'start_time',
            'end_time',
        ]


class VideoMakerSerializer(serializers.ModelSerializer):
    duration = DuratinSeriaizer()
    class Meta:
        model = VideoMaker
        fields = [
            'id',
            'typee',
            'high_volume',
            'low_volume',
            'video_component_id',
            'url',
            'duration',
        ]

    def create(self, validated_data):
        duration_data = validated_data.pop('duration')
        duration_serializer = DuratinSeriaizer(data=duration_data)
        duration_serializer.is_valid(raise_exception=True)
        duration = duration_serializer.save()
        validated_data['duration'] = duration
        video_maker = VideoMaker.objects.create(**validated_data)
        return video_maker
