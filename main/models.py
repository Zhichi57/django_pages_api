from django.db import models
from ordered_model.models import OrderedModel


class Video(models.Model):
    class Meta:
        db_table = 'videos'

    title = models.CharField(max_length=255)
    video_ulr = models.URLField()
    subtitles_ulr = models.URLField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Audio(models.Model):
    class Meta:
        db_table = 'audios'

    title = models.CharField(max_length=255)
    bitrate = models.IntegerField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Text(models.Model):
    class Meta:
        db_table = 'texts'

    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


class Page(models.Model):
    class Meta:
        db_table = 'pages'

    title = models.CharField(max_length=255)
    videos = models.ManyToManyField(Video, through='PageVideosThroughModel')
    audios = models.ManyToManyField(Audio, through='PageAudiosThroughModel')
    texts = models.ManyToManyField(Text, through='PageTextThroughModel')

    def __str__(self):
        return f"{self.title}"


class PageTextThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.text.id}"


class PageVideosThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.video.id}"


class PageAudiosThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.audio.id}"
