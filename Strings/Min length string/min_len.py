## Read input as specified in the question.
## Print output as specified in the question.
words = [x for x in input().split()]
min_len = 10**5
min_word = ''
for word in words:
    #print(word, len(word), 'min_len ', min_len)
    if len(word) < min_len:
        
        min_len = len(word)
        min_word = word
print(min_word)
