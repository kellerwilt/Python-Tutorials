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
        print 'They forgot to lock you in. You escape and roam free forever'
        trapped = False
        break
    temp = raw_input('Press enter to continue')
    