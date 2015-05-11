import random
import math
import string
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
    temp_number1 /= len(words_input)
    size = temp_number1 + abs(temp_number1 - temp_number2) + math.sqrt(temp_number1) 
    print size
    temp_number2 = 0 
    temp_number1 = 0
    grid = []
    size = int(size)+1
    for i in range(0,size):
        grid.append([])
    for i in range(0,size):
        for o in range(0,size):
            grid[i] += ' '
    for word in words_input:
        safe=True
        while safe:
            safe = True
            word_direction = directions[random.randint(0,1)]
            if word_direction == "up":
                startx = random.randint(0,size-1)
                starty = random.randint(len(word)-1,size-1)
                tempx  = startx
                tempy  = starty
                for i in range(0,len(word)):
                    if grid[tempx][tempy] != ' ':
                        if grid[tempx][tempy] == word[i]:
                            tempy -= 1
                        else:
                            safe = False
                            break
                if safe:
                    for i in range(0,len(word)):
                        grid[startx][starty] = word[i]
                        starty-=1
                    safe = False
            if word_direction == "downleft":
                startx = random.randint(0,size-len(word)-1)
                starty = random.randint(len(word)-1,size-1)
                tempx  = startx
                tempy  = starty
                for i in range(0,len(word)):
                    if grid[tempx][tempy] != ' ':
                        if grid[tempx][tempy] == word[i]:
                            tempy -= 1
                            tempx += 1
                        else:
                            safe = False
                            break
                    else:
                        tempy-=1
                        tempx+=1
                if safe:
                    for i in range(0,len(word)):
                        grid[startx][starty] = word[i]
                        starty-=1
                        startx+=1
                    safe = False
    print_board(grid)
def print_board(grid):
    for i in grid:
        for o in i:
            print o,
        print ''
print 'Word Search:'
print word_search(['hat','pat','hut','put','walrus'])