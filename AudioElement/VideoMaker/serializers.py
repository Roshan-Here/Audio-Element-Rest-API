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

    
        # print(validated_data.id)
        # print(data.pk)
    #     return VideoMaker.objects.create(**validated_data)

    # def create(self, validated_data):
    #     albums_data = validated_data.pop('album_musician')
    #     musician = Musician.objects.create(**validated_data)
    #     for album_data in albums_data:
    #         Album.objects.create(artist=musician, **album_data)
    #     return musician


        # set video_duration.id = videomaker.id->