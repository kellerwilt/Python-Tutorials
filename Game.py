def room():
    trapped = True
    while trapped: 
        print 'You wake up in a strange room. There is a mirror, a table and a window. What do you do to escape?'
        temp = raw_input('Press enter to continue')
        print ''
        print 'A: Climb out the window'
        print 'B: Wait for someone to find you'
        print 'C: Climb through the mirror into the matrix'
        print 'D: Open the door'
        answer=raw_input('Which option do you choose (a,b,c,d)').upper()
        if answer == 'A':
            print 'The window is locked, and will not open'
        if answer == 'B':
            print 'You wait 15 days, and nobody arrives to help you'
        if answer == 'C':
            print "You dive through the mirror, and hurt your head. This mirror doesn't lead to the matrix"
        if answer == 'D': 
            print 'They forgot to lock you in. You escape and enter a seemingly endless hallway.'
            trapped = False
            temp = raw_input('Press enter to continue')
            break
        temp = raw_input('Press enter to continue')
def hallway():
    in_hallway = True
    while in_hallway:
        print 'You look down the hallway, and it seems to go on forever. Along the walls, are doors, each one different from the next. What do you do?'
        temp = raw_input('Press enter to continue')
        print ''
        print 'A: Walk down the hallway to see where it leads'
        print 'B: Start trying doors to see where they go'
        print 'C: Go back to the room to see if you missed something'
        print 'D: Yell down the hall to see if anyone else is there'
        answer=raw_input('Which option do you choose (a,b,c,d)').upper()
        if answer == 'A':
            print 'You wander aimlessly for 10 minutes. You begin to realize the doors are repeating themselves, and that you have been going in circles.'
        if answer == 'B':
            print "You start going through the doors, they all lead to dreams you have had in the past. You eventually get to a door covered in a zebra stripe pattern. You open it and it leads to what looks like your house. You enter, out of curiousity."
            in_hallway = False
            temp = raw_input('Press enter to continue')
            break
        if answer == 'C':
            print "You enter the room again, and look everywhere you can, but you don't notice anything you didn't see before."
        if answer == 'D':
            print 'Your voice echoes eerily around you. You wait, but hear nothing but your own panicked breath.'
def house():
    in_house = True
    is_tired = True
    times_eaten = 0
    while in_house:
        print "It's a perfect replica of your house, but no decisions jump out at you immediately."
        temp = raw_input('Press enter to continue')
        print ''
        print "A: Go to your kitchen and get something to eat"
        print "B: Go to the front door and leave"
        print "C: Go back to the hallway to see if you missed anything"
        print "D: Go to bed and see if this is all a dream"
        answer = raw_input('Which option do you choose (a,b,c,d)').upper()
        if answer == 'A':
            if times_eaten < 3:
                print "You eat a normal meal, and nothing seems out of the ordinary"
                times_eaten += 1
            else:
                print "You have run out of food"
        if answer == 'B':
            print "You go outside and I run out of ideas"
            in_house = False
            break
        if answer == 'C':
            print "The hallway looks exactly as it did before"
            hallway()
        if answer == 'D':
            if is_tired:
                print "You have a peaceful, unninterupted nap. Now that you are rested, you return to your investigation."
                is_tired = False
            else:
                print "You lie in bed for some time, but are not tired enough to fall asleep."   
room()
hallway()
house()
print 'Congratulations! You have outlived my immagination!'
temp = raw_input('Press enter to win')