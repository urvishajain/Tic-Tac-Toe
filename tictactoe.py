tboard= {
    '1':' ', '2':' ','3':' ',
    '4':' ','5':' ','6':' ',
    '7':' ', '8':' ','9':' '
}
def printboard(board):
    print(board['1']+'|'+board['2']+'|'+board['3'])
    print('-+-+-')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-+-+-')
    print(board['7']+'|'+board['8']+'|'+board['9'])
cnt=0    
printboard(tboard)    
turn='0'
for i in range(9):
    print('Turn for '+turn+' ,Move to which space?')
    move=input()
    tboard[move]=turn
    printboard(tboard)
    if((tboard['1']==turn and tboard['2']==turn and tboard['3']==turn) or (tboard['1']==turn and tboard['4']==turn and tboard['7']==turn) or (tboard['4']==turn and tboard['5']==turn and tboard['6']==turn) or (tboard['7']==turn and tboard['8']==turn and tboard['9']==turn) or (tboard['2']==turn and tboard['5']==turn and tboard['8']==turn) or (tboard['3']==turn and tboard['6']==turn and tboard['9']==turn) or (tboard['1']==turn and tboard['5']==turn and tboard['9']==turn) or (tboard['3']==turn and tboard['5']==turn and tboard['7']==turn)):
        print(turn+ ' won')
        cnt=1
        break; 
    if(turn=='X'):
       
        turn='0'
    else: 
        
        turn='X' 
         
if(cnt==0) :
    print('TIE HO GAYA')
