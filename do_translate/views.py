from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import filters
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .serializers import *


class EnglishWordViewSet(ModelViewSet):
	queryset = EnglishWord.objects.all()
	serializer_class = EnglishWordSerializer
	# filter_backends = [DjangoFilterBackend, ]
	# filter_class = EnglishWordFilter
	# search_fields = ('english_word',)
	#filter_backends = [filters.SearchFilter]
	#search_fields = ['english_word', ]


class HindiMeaningViewSet(ModelViewSet):
	queryset = HindiMeaning.objects.all()
	serializer_class = HindiMeaningSerializer


def index(request):
	return render(request, 'index.html')


class MatchingWordList(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'search_list.html'

	def get(self, request, ):
		english_word = request.query_params['english_word']

		best_match = EnglishWord.objects.filter(english_word=english_word)
		best_match = EnglishWordSerializer(best_match, many=True).data

		similar_match = EnglishWord.objects.filter(
			Q(english_word__icontains=english_word) & ~Q(english_word=english_word))[0:20]
		similar_match = EnglishWordSerializer(similar_match, many=True).data

		data = {'best_match': best_match, 'similar_match': similar_match}
		return Response(data)


class EnglishWordList(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'english_word_list.html'

	def get(self, request):
		queryset = EnglishWord.objects.all()[0:50]
		return Response({'english_words': queryset})


class EnglishWordDetail(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'english_word_detail.html'

	def get(self, request, pk):
		english_word = get_object_or_404(EnglishWord, pk=pk)
		# serializer = EnglishWordSerializer(english_word)
		# {'serializer': serializer, 'english_word': english_word}

		# hindi results
		all_hindi_translations = HindiMeaning.objects.filter(english_word=english_word)
		all_hindi_translations = HindiMeaningSerializer(all_hindi_translations, many=True).data

		return Response({'all_hindi_translations': all_hindi_translations, 'english_word': english_word})
