import pyshorteners 
import os
import time
import rainbowtext, pyfiglet

class color : 
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'
print(f'{color.GREEN}'
          ' ╔═════════════════════════════════╗\n'
          ' ║ telegram -> https://t.me/Difalio║\n'
          ' ║ link Shortner                   ║\n'
          ' ║ Author: Telepathic              ║\n'
          ' ╚═════════════════════════════════╝\n')
link = input(f"{color.GREEN}enter the link: {color.RED}")
shortener=pyshorteners.Shortener()

shortener_link=shortener.tinyurl.short(link)

print(f"{color.GREEN}#########1{color.WHITE}")
time.sleep(1)
print(f"{color.WHITE}##################2{color.WHITE}")
time.sleep(1)
print(f"{color.RED}###########################3{color.WHITE}")
print(f"\n{color.GREEN}Shorted Link is: {color.RED}",shortener_link)
