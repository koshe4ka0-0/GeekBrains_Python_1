import random
import card
import os

lst_all = [itm for itm in range(1, 91)]
lst = [itm for itm in range(1, 91)]

random.shuffle(lst)

player = [lst[itm] for itm in range(0, 15)]

computer  = [lst[itm] for itm in range(15, 30)]

computer_card = card.players_card(computer)

play_card = card.players_card(player)


comp = 15
play = 15

while comp != 0 and play != 0:
    print(play)
    print(comp)
 
    print(computer_card.fillcard(computer))
    print(play_card.fillcard(player))

    numb = random.sample(lst_all, 1)[0]
    print(numb)
    lst_all.remove(numb)
    
    
    if numb in computer_card.lst:
        computer_card.step(numb)
        comp -= 1
    
    answer = input("Хотите ли вы зачеркнуть число? Y/N ")
    
    if answer is 'Y':
        if numb in play_card.lst:
            play_card.step(numb)
            play -= 1
        else:
            print("Вы проиграли ")
            break
    else: 
        pass

    os.system('CLS')

if comp == 0:
    print("Вы проиграли ")

elif play == 0:
    print("Вы выйграли! ")

