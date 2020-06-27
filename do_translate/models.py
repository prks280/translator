from django.db import models


class EnglishWord(models.Model):
	english_word = models.CharField(max_length=1000)

	def __str__(self):
		return self.english_word


class HindiMeaning(models.Model):
	english_word = models.ForeignKey(EnglishWord, on_delete=models.CASCADE)
	hindi_meaning = models.CharField(max_length=1000)
	grammar = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.english_word, self.hindi_meaning
