from main.models import *
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url']
        ordering = ['-id']


class InfoPageSerializer(serializers.ModelSerializer):
    texts = TextSerializer(read_only=True, many=True)
    videos = VideoSerializer(read_only=True, many=True)
    audios = AudioSerializer(read_only=True, many=True)

    class Meta:
        model = Page
        fields = ['title', 'videos', 'audios', 'texts']
