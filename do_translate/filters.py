import django_filters

from .models import *


class EnglishWordFilter(django_filters.FilterSet):
	class Meta:
		model = EnglishWord
		fields = {
			'english_word': ['exact', 'icontains'],
		}
