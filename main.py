from colorama import Fore, Back, Style, init
import pyfiglet
import random

T = "BitePasswordGen"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

def GenPass(taille):
    carractere = "&~#'{([-|è_\ç^à@))=+°0987654321€$£*ùazertyuiopqsdfghjklmwxcvbn><,?;.:/!§"
    pwd = ''.join(random.choice(carractere)for i in range(taille))
    return pwd
       
while True :  
    print(Fore.GREEN+"")
    taille = int(input("taille :"))
    mdp = GenPass(taille)
    if taille <= 10 :
        print(Fore.RED+"bad password : need more lenght")
    elif taille <= 20 :
        print(Fore.YELLOW+"medium password : need more lenght")
    else:
        print(Fore.GREEN+"strong password")
    print(Fore.WHITE+mdp)
    print("\n")
