# counting 'the'
text = input().split(' ')
text2 = []
for word in text:
    word = word.strip(',.')
    text2.append(word)
print(text2.count('the'))
