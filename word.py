from textblob import TextBlob
a = TextBlob("CampK12 is a good compny and alays valule ttheir employeees.")
b = a.correct()
print(a)
print(b)
word = TextBlob("bonjour")
lan = word.detect_language()
print(lan)