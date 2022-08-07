from django.db import models


class Video(models.Model):
    class Meta:
        db_table = 'videos'

    title = models.CharField(max_length=255)
    video_ulr = models.URLField()
    subtitles_ulr = models.URLField()
    counter = models.IntegerField()


class Audio(models.Model):
    class Meta:
        db_table = 'audios'

    title = models.CharField(max_length=255)
    bitrate = models.IntegerField()
    counter = models.IntegerField()


class Text(models.Model):
    class Meta:
        db_table = 'texts'

    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    counter = models.IntegerField()


class Page(models.Model):
    class Meta:
        db_table = 'pages'
        ordering = ['id']

    title = models.CharField(max_length=255)
    videos = models.ManyToManyField(Video)
    audios = models.ManyToManyField(Audio)
    texts = models.ManyToManyField(Text)
