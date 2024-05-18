from collections import Counter

def question_1(text):
    counter = Counter(text)
    result = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    return result
#text = "Hello, World!"
text = "sdasaa"
print(question_1(text))
