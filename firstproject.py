import random
'''
# snake=0
# water=1
# gun=-1
'''

computer= random.choice([-1,0,1])
youstr=(input('enter your choise: '))
youdict={'s': 0, 'w': 1, 'g': -1}
reversedict ={0:'snake', 1:'water', -1:'gun'}
you=youdict[youstr]
print(f'you selected {reversedict[you]}\ncomputer selected {reversedict[computer]}')

if(computer==you):
    print('its a draw')
else:
    if(computer==0 and you==1):
        print('you lose!')    
    elif(computer==0 and you==-1):
        print('you win!')    
    elif(computer==1 and you==0):
        print('you win!')    
    elif(computer==1 and you==-1):
        print('you lose!')    
    elif(computer==-1 and you==0):
        print('you lose!')    
    elif(computer==-1 and you==1):
        print('you win!')    
    else:
     print('something went wrong')    