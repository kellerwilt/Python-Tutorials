import random
def word_scramble(words_input):
    words_scrambled = []
    temp = ''
    for i in words_input:
        temp = ''
        for o in range(0,len(i)):
            random_letter = random.randint(0,len(i)-1)
            temp += i[random_letter]
            i = i[0:random_letter] + i[random_letter+1:]
        words_scrambled.append(temp)
    return words_scrambled
print word_scramble(["maybe","this","works"])
def
