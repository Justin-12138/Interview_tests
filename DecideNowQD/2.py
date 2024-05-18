def question_2(text, word):
    count = 0
    index_list = []
    index = text.find(word)
    while index != -1:
        count += 1
        index_list.append(index)
        index = text.find(word, index + 1)
    return count, index_list
text = "我买了华为的手机，因为华为手机的芯片是自研的"
word = "手机"
count, index_list = question_2(text, word)
print("count:", count)
print("index list:", index_list)
