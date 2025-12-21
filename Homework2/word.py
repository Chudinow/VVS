second_text = input()
print("your favourite word")
word = input()
word_1 = 'круто'
index = second_text.find(word_1) 
second_text = second_text.replace(word_1, word)
print(second_text, second_text.count('о'))
