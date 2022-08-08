from django.db import models
from ordered_model.models import OrderedModel


# Модель для контента типа "Видео"
class Video(models.Model):
    class Meta:
        db_table = 'videos'

    title = models.CharField(max_length=255)
    video_ulr = models.URLField()
    subtitles_ulr = models.URLField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


# Модель для контента типа "Аудио"
class Audio(models.Model):
    class Meta:
        db_table = 'audios'

    title = models.CharField(max_length=255)
    bitrate = models.IntegerField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


# Модель для контента типа "Текст"
class Text(models.Model):
    class Meta:
        db_table = 'texts'

    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"


# Модель для сущности "Страница"
class Page(models.Model):
    class Meta:
        db_table = 'pages'

    title = models.CharField(max_length=255)
    videos = models.ManyToManyField(Video, through='PageVideosThroughModel')
    audios = models.ManyToManyField(Audio, through='PageAudiosThroughModel')
    texts = models.ManyToManyField(Text, through='PageTextThroughModel')

    def __str__(self):
        return f"{self.title}"


# Модель для связи сущности "Страница" с контентом типа "Текст"
class PageTextThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.text.id}"


# Модель для связи сущности "Страница" с контентом типа "Видео"
class PageVideosThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.video.id}"


# Модель для связи сущности "Страница" с контентом типа "Аудио"
class PageAudiosThroughModel(OrderedModel):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE)
    order_with_respect_to = 'page'

    class Meta:
        ordering = ('page', 'order')

    def __str__(self):
        return f"ID: {self.audio.id}"
