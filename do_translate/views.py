from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .serializers import *
from .filters import *
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import mixins
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q


class EnglishWordViewSet(ModelViewSet):
	queryset = EnglishWord.objects.all()
	serializer_class = EnglishWordSerializer
	# filter_backends = [DjangoFilterBackend, ]
	# filter_class = EnglishWordFilter
	# search_fields = ('english_word',)
	filter_backends = [filters.SearchFilter]
	search_fields = ['english_word', ]


class HindiMeaningViewSet(ModelViewSet):
	queryset = HindiMeaning.objects.all()
	serializer_class = HindiMeaningSerializer


def index(request):
	return render(request, 'index.html')


class MatchingWordList(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'profile_list.html'

	def get(self, request, ):
		english_word = request.query_params['english_word']

		best_match = EnglishWord.objects.filter(english_word=english_word)
		best_match = EnglishWordSerializer(best_match, many=True).data

		similar_match = EnglishWord.objects.filter(
			Q(english_word__icontains=english_word) & ~Q(english_word=english_word))[0:20]
		similar_match = EnglishWordSerializer(similar_match, many=True).data

		data = {'best_match': best_match, 'similar_match': similar_match}
		return Response(data)


class AllHindiMeanings(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'all-hindi-meanings.html'

	def get(self, request, pk):
		word = get_object_or_404(EnglishWord, pk=pk)
		serializer = EnglishWordSerializer(word)
		return Response({'serializer': serializer, 'word': word})
