import csv
from do_translate.models import *

with open('1_English-Hindi Dictionary.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	total = 173100
	for row in csv_reader:
		try:
			english_word, hindi_meaning, grammar = row[0], row[1], row[2]
			try:
				english = EnglishWord.objects.get(english_word=english_word)
			except:
				english = EnglishWord.objects.create(english_word=english_word)
			hindi = HindiMeaning.objects.create(english_word=english, hindi_meaning=hindi_meaning, grammar=grammar)
			print(total - 1, english_word)
		except Exception as e:
			print('****** error :', e)
		total -= 1

#TODO few english words are empty
#TODO navigation


# <!--<button id="myButton" class="float-left submit-button" >Home</button>-->
#
# <!--<script type="text/javascript">-->
# <!--    document.getElementById("myButton").onclick = function () {-->
# <!--        location.href = "www.yoursite.com";-->
# <!--    };-->
# <!--</script>-->
#
# <!--<button onclick="displayDate()">The time is?</button>-->
#
# <!--<script>-->
# <!--function displayDate() {-->
# <!--  document.getElementById("demo").innerHTML = Date();-->
# <!--}-->
# <!--</script>-->
# <!--<p id="demo"></p>-->
