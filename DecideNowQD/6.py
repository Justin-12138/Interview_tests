def question_6(text):
    max_count = 0
    max_char = ''
    prev_char = ''
    count = 0
    for char in text:
        if char == prev_char:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = char
        prev_char = char

    return max_char, max_count
text = "165896514101ddnidndngooooooeur15541"
char, count = question_6(text)
print("char:", char)
print("count:", count)
