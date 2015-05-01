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
print 'Word Scramble:'
print word_scramble(["maybe","this","works"])
def word_search(words_input):
    temp_number1 = 0
    temp_number2 = 0
    temp_string = ''
    directions = ["up","upright","right","downright","down","downleft","left","upleft"]
    for i in words_input:
        temp_number1 += len(i)
        if len(i)>temp_number2:
            temp_number2 = len(i)
    print temp_number1
    temp_number1 /= len(words_input)
    size = temp_number1 + abs(temp_number1 - temp_number2)
    print size
    temp_number2 = 0 
    temp_number1 = 0
    grid = []
    for i in range(0,size):
        grid.append([])
    for i in range(0,size):
        for o in range(0,size):
            grid[i] += 'X'
    for i in words_input:
        word_direction = directions[random.randint(0,7)]
    print_board(grid)
def print_board(grid):
    for i in grid:
        for o in i:
            print o,
        print ''
print 'Word Search:'
print word_search(["maybe","this","works","but","maybe","not","because",'my','size','algorithm','might','be','flawed'])