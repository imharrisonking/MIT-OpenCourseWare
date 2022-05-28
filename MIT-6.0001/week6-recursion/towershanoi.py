def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to) # base case when tower is of height 1
    else:
        Towers(n-1, fr, spare, to) # take a tower of n-1 and move it from 'from' to 'spare'
        Towers(1, fr, to, spare) # move the left over disc (at the very bottom of pile) from 'from' to 'to' (it's final destination)
        Towers(n-1, spare, to, fr) # move the rest of the tower at 'spare' to 'to'

print(Towers(4, 'P1', 'P2', 'P3'))