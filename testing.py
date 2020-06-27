import csv
from do_translate.models import *
import time

with open('1_English-Hindi Dictionary.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		try:
			english_word = row[0]
			hindi_meaning = row[1]
			grammar = row[2]
			try:
				english = EnglishWord.objects.get(english_word=english_word)
				if english:
					print('this word is repeated', english_word)
			except:
				english = EnglishWord.objects.create(english_word=english_word)
			hindi = HindiMeaning.objects.create(english_word=english, hindi_meaning=hindi_meaning, grammar=grammar)
		except Exception as e:
			print('****** error :', e)
