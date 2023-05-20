from django.db import models

# Create your models here.

class VideoMaker(models.Model):
    # "type": <vo|bg_music|video_music>",
    CHOICE_SELECT = (
        ('vo'),
        ('bg_music'),
        ('video_music'),
    )
    type = models.CharField(max_length=15,choices=CHOICE_SELECT)
    high_volume = models.PositiveIntegerField()
    low_volume = models.PositiveIntegerField()
    video_component_id = models.CharField(max_length=300,null=True,blank=True)
    url = models.URLField(blank=True,null=True)
    start_time = models.PositiveIntegerField(blank=True,null=True)
    end_time = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.id