from random import randint
from time import sleep

atk=randint(1,20)

print(f'O valor do ataque é: {atk}')

sleep(1)

defe=randint(1,20)

print(f'O valor da defesa é: {defe}')

sleep(1.5)

if defe > atk:
    print('DEFESA SUPREMA!')
    dano=0

elif atk % 2 == 0:
    print('DANO CRITICO!')
    dano=atk*2
    dano-=defe

else:
    print('BONUS DE ATK IMPAR!')
    dano=atk+10
    dano-=defe

print(f'O DANO FINAL FOI: {dano}')