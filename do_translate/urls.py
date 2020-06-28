from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('english_word', EnglishWordViewSet, basename='english_word')
router.register('hindi_meaning', HindiMeaningViewSet, basename='hindi_meaning')

urlpatterns = router.urls

