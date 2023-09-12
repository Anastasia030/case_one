from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from googletrans import Translator, constants
# nltk.download('movie_reviews')
# nltk.download('punkt')

text = input("Введите текст:") #почистить пробелы

translator = Translator()
translation = translator.translate(text)
# print(translation.src)
print(translation.text)

if translation.src == 'ru':
    text = translation.text

# print(text)
out = TextBlob(text).correct()
text_one = TextBlob(
    text,
    analyzer=NaiveBayesAnalyzer(),
)

text_blob_object = TextBlob(text)
text_sentence = text_blob_object.sentences
# print(text_sentence)
text_words = text_blob_object.words
# print(text_words)

vowels = ['E', 'Y', 'U', 'I', 'O', 'A']
text_separ = text_blob_object.words.singularize()
v_count = 0
for i in range(len(text_separ)):
    for j in text_separ[i]:
        if j in vowels or j.upper() in vowels:
            v_count += 1

ASL = len(text_words) / len(text_sentence)
ASW = v_count / len(text_words)
K = 206.835 - 1.015 * ASL - 84.6 * ASW
K_ru = 206,835 - 1,3 * ASL - 60,1 * ASW


t0 = TextBlob(text)
t = t0
ton = t.polarity
if (ton >= -1.0) and (ton < 0):
    analysis_ton = 'Негативный'
elif (ton > 0) and (ton <= 1.0):
    analysis_ton = 'Положительный'
elif ton == 0:
    analysis_ton = 'Нейтральный'


print('Предложений:', len(text_sentence))
print('Слов:', len(text_words))
print('Слогов:', v_count)
print('Средняя длина предложений в слогах:', ASL)
print('Средняя длина слов в слогах:', ASW)
print('Индекс удобочитаемости Флеша:', K)

if K > 50:
    if K > 80:
        print('Текст очень легко читается (для младших классов)')
    else:
        print('Простой текст (для школьников)')
else:
    if K > 25:
        print('Текст немного трудно читать (для студентов)')
    else:
        print('Текст трудно читать (для выпускников ВУЗов)')

print('Тональность текста:', analysis_ton)
print('Объективность:', round(1 - TextBlob(text).subjectivity, 2) * 100, '%', sep='')