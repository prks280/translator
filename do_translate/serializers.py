from rest_framework import serializers
from .models import *


class EnglishWordSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnglishWord
		fields = '__all__'


class HindiMeaningSerializer(serializers.ModelSerializer):
	english_word = serializers.CharField(source='english_word.english_word', read_only=True)

	class Meta:
		model = HindiMeaning
		fields = ('english_word', 'hindi_meaning', 'grammer')
