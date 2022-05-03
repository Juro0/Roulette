from objects import *
from colorama import Fore as f
from colorama import Style as s
import os
import time
import random

# Nomi di default, hanno solo valore affettivo e simbolico, tanto vengono sovrascritti
p1 = Player(name='Juri')
p2 = Player(name='Alibi')
p3 = Player(name='Nello Taver')
p4 = Player(name='Pino')

possibili = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","nero","rosso"]

all = [uno, due, tre, quattro, cinque, sei, sette, otto, nove, dieci, undici, dodici, tredici, quattordici, quindici, sedici, diciasette, diciotto, diciannove, venti, ventuno, ventidue, ventitre, ventiquattro, venticinque, ventisei, ventisette, ventotto, ventinove, trenta, trentuno, trentadue, trentatre, trentaquattro, trentacinque, trentasei]

def clear():
    os.system('cls')

# SCELTA ROULETTE - simula un giro di roulette con una generazione pseudo-randomica
def sceltaRoulette():
    scelta = random.choice(all)
    return scelta

# CHECK - controlla se un player ha vinto e nel caso aumenta i soldi
def check(player, vic):

    choice = player.get_play()

    if choice == "SQUALIFICATO":
        return "SQUALIFICATO"
    else:
        if choice.lower() == vic.get_color().lower():
            player.add_cash(player.get_scommessa())
            return f'{player.get_name()} ha vinto puntando sul {player.get_play()} e ora ha {player.get_cash()}$'

        elif str(choice) == str(vic.get_value().lower()):
            player.add_cash(player.get_scommessa()*2)
            return f'{player.get_name()} ha vinto puntando sul {player.get_play()} e ora ha {player.get_cash()}$'
        
        else:
            player.sub_cash(player.get_scommessa())
            return f'{player.get_name()} non ha vinto nulla, e la sua fortuna ora è a {player.get_cash()}$'

# PUNTA - carica la schermata che permette al player di puntare su un numero.
#   se il giocatore è squalificato viene saltato
def punta(player):
    clear()

    if player.get_cash() <= 0:
        print(f'{f.RED} {player.get_name()} non hai più soldi! Sei squalificato.')
        player.select_play("SQUALIFICATO")
        time.sleep(2)
    else:
        print(f'{f.GREEN} {player.get_name()} inserisci la tua puntata. (1-36 o nero-rosso)')
        
        puntata = input(f'{s.RESET_ALL}> ')

        if puntata in possibili:
            pass
        else:
            punta(player)
        
        player.select_play(puntata)

        print(f'{f.GREEN} {player.get_name()} hai puntato sul {player.get_play()}!\n Quanti soldi vorresti scommettere? (1-{player.get_cash()})')

        scommessa = input(f'{s.RESET_ALL}> ')

        scommessa = int(scommessa)

        if scommessa > 0 and scommessa <= player.get_cash():
            player.select_scommessa(scommessa)
        if scommessa <= 0 or scommessa > player.get_cash():
            punta(player)

# NEW GAME - inizia una nuova partita
def newGame():
    clear()
    
    punta(p1)
    punta(p2)
    punta(p3)
    punta(p4)

    scelta = sceltaRoulette()

    for i in range(5):
        clear()
        print(f'{f.RED} La roulette sta girando!\n')
        print(' '+'▮▮▮'*i)
        time.sleep(1)
    
    clear()

    print(f'{f.GREEN} ha vinto il numero {scelta.get_value()}, di colore {scelta.get_color()}!\n')

    print( s.RESET_ALL + " " + check(p1, scelta) )
    print( s.RESET_ALL + " " + check(p2, scelta) )
    print( s.RESET_ALL + " " + check(p3, scelta) )
    print( s.RESET_ALL + " " + check(p4, scelta) )

    print(f'\n{f.GREEN} premi invio per continuare...')
    input(f'{s.RESET_ALL} >')

    main()

# MAIN - schermata iniziale
def main():
    clear()
    print(f'{f.RED} Roulette Francese - by Juro\n')
    print(f'{f.GREEN} Giocatori in gioco e saldo:')
    print(f'{s.RESET_ALL} {p1.get_name()}: {p1.get_cash()}$')
    print(f'{s.RESET_ALL} {p2.get_name()}: {p2.get_cash()}$')
    print(f'{s.RESET_ALL} {p3.get_name()}: {p3.get_cash()}$')
    print(f'{s.RESET_ALL} {p4.get_name()}: {p4.get_cash()}$')
    print()
    print(f'{f.GREEN} Scrivi "start" per iniziare una nuova mano!')

    input(f'{s.RESET_ALL}> ')
    newGame()

if __name__ == '__main__':

    p1.set_name( input('Inserisci il nome del player 1: ') )
    p2.set_name( input('Inserisci il nome del player 2: ') )
    p3.set_name( input('Inserisci il nome del player 3: ') )
    p4.set_name( input('Inserisci il nome del player 4: ') )

    main()