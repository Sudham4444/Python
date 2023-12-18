numbers=[1,2,3,4]
print(numbers)
words=["word1",'word2',3,4.5,6,None]
print(words[:2])
print(words[-1])

words[1]="word22"
print(words)
words[1:]="three"
print(words)
words[1:]=["three"]
print(words)