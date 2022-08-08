from main.models import *
from rest_framework import serializers


# Сериализатор для списка страниц
class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url']
        ordering = ['-id']


# Сериализатор для списка контента типа текст
class PageTextThroughSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='text.title')
    value = serializers.CharField(source='text.value')
    counter = serializers.IntegerField(source='text.counter')

    class Meta:
        model = PageTextThroughModel
        fields = ('title', 'value', 'counter')


# Сериализатор для списка контента типа видео
class PageVideosThroughSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='video.title')
    video_ulr = serializers.CharField(source='video.video_ulr')
    subtitles_ulr = serializers.CharField(source='video.subtitles_ulr')
    counter = serializers.IntegerField(source='video.counter')

    class Meta:
        model = PageVideosThroughModel
        fields = ('title', 'video_ulr', 'subtitles_ulr', 'counter')


# Сериализатор для списка контента типа аудио
class PageAudiosThroughSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='audio.title')
    bitrate = serializers.CharField(source='audio.bitrate')
    counter = serializers.IntegerField(source='audio.counter')

    class Meta:
        model = PageAudiosThroughModel
        fields = ('title', 'bitrate', 'counter')


# Сериализатор для подробной информации о странице
class InfoPageSerializer(serializers.ModelSerializer):
    texts = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()
    audios = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['title', 'videos', 'audios', 'texts']

    # Получение упорядоченного списка контента типа текст
    def get_texts(self, obj):
        qset = PageTextThroughModel.objects.filter(page_id=obj)
        return [PageTextThroughSerializer(m).data for m in qset]

    # Получение упорядоченного списка контента типа видео
    def get_videos(self, obj):
        qset = PageVideosThroughModel.objects.filter(page_id=obj)
        return [PageVideosThroughSerializer(m).data for m in qset]

    # Получение упорядоченного списка контента типа аудио
    def get_audios(self, obj):
        qset = PageAudiosThroughModel.objects.filter(page_id=obj)
        return [PageAudiosThroughSerializer(m).data for m in qset]
