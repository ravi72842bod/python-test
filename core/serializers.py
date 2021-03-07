from rest_framework import serializers
from core.models import *

class SongSerializer(serializers.ModelSerializer):

	class Meta:
		model = SongModel
		fields = '__all__' 

class PodcastSerializer(serializers.ModelSerializer):

	class Meta:
		model = PodcastModel
		fields = '__all__'


class AudiobookSerializer(serializers.ModelSerializer):

	class Meta:
		model = AudiobookModel
		fields = '__all__'