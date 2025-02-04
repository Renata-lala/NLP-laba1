# -*- coding: utf-8 -*-
"""НЛП-лаба1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O1ngoC9djOU-ssKmHG5X8w-t4T-JAfWb

**Лабораторная работа №1**
Юнусова Рената 932101
"""

#Токенизация
import nltk
from nltk.tokenize import word_tokenize

#Сегментация
import nltk
from nltk import sent_tokenize

#Лемматизация
import pymorphy2
m = pymorphy2.MorphAnalyzer()

text = open('text.txt', 'r', encoding='utf-8')
text = text.read()
print('исходный текст:')
print(text)

sentences = sent_tokenize(text)

print('Итог:')
for i in sentences:
  words = word_tokenize(i)
  for j in range (len(words)-1):
    word_1 = words[j]
    word_2 = words[j+1]
    parse_1 = m.parse(word_1)[0]
    parse_2 = m.parse(word_2)[0]
    #проверка на то, что имеются ли имена существительные или имена прилагательные на первом или втором месте
    if ((parse_1.tag.POS == 'NOUN') | (parse_1.tag.POS == 'ADJF')) & ((parse_2.tag.POS == 'NOUN') | (parse_2.tag.POS == 'ADJF')):
      #проверка на подеж
      if parse_1.tag.case == parse_2.tag.case:
        #проверка на род
        if parse_1.tag.gender == parse_2.tag.gender:
          #проверка на число
          if parse_1.tag.number == parse_2.tag.number:
            print(parse_1.normal_form, parse_2.normal_form)