def is_palindrome(word):
    reversed_word=word[::-1] 
    if word == reversed_word:
        return True
    return False
word=input("enter a word to check: ")
print(is_palindrome(word))




def is_palindrome1(word1):
    if word == word1[::-1]:
        return True
    return False
word1=input("enter a word to check: ")
print(is_palindrome1(word1))



def is_palindrome2(word2):
    return word2 == word2[::-1]
word2=input("enter a word to check: ")
print(is_palindrome2(word2))


