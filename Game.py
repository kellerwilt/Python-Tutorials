trapped = True
while trapped: 
    print 'You wake up in a strange room. There is a mirror, a table and a window. What do you do to escape?'
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
in_hallway = True
while in_hallway:
    print 'You look down the hallway, and it seems to go on forever. Along the walls, are doors, each one different from the next. What do you do?'
    print 'A: Walk down the hallway to see where it leads'
    print 'B: Start trying doors to see where they go'
    print 'C: Go back to the room to see if you missed something'
    print 'D: Yell down the hall to see if anyone else is there'
    answer=raw_input('Which option do you choose (a,b,c,d)').upper()
    if answer == 'A':
        print 'You wander aimlessly for 10 minutes. You begin to realize the doors are repeating themselves, and that you have been going in circles.'
    if answer == 'B':
        print "You start going through the doors, they all lead to dreams you have had in the past. You eventually get to a door covered in a zebra stripe pattern. You open it and it leads to a replica of your house. The model is so accurate it's uncanny. Every detail is correct. You enter, out of curiousity."
        in_hallway = False
        temp = raw_input('Press enter to continue')
        break
        
    if answer == 'C':
        print "You enter the room again, and look everywhere you can, but you don't notice anything you didn't see before."
    if answer == 'D':
        print 'Your voice echoes eerily around you. You wait, but hear nothing but your own panicked breath.'