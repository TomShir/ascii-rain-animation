#Simulate rain in vscode terminal
from colorama import Fore 
import time 
import sys 
import random 
rain_text='rain...'
def loop_over(text,color,delay_time):
   for n in text:
      sys.stdout.flush()
      time.sleep(delay_time)
      sys.stdout.write(f'{color}{n}')
   else:
      print(f'{Fore.RESET}')
      
loop_over(text=rain_text,color=Fore.BLACK,delay_time=0.1)
time.sleep(1)
print('\n')
time.sleep(1)
for n in range(2000):
 backslash_character=['\n','\b','\t']
 random_backslash_character=random.choice(backslash_character)
  rain_frames=['|',' |','  |','    |','     |','      |','       |','        |','         |','          |','            |','             |         ','           | ','                   |','                      |','                               |','                                       |','                                                     |','                                                                                 |','                                                                              |','                                                                                                |','                                                                                                                 |']
 random_rain_frame=random.choice(rain_frames)
 print(f'{Fore.BLACK}{random_rain_frame}{random_backslash_character}')
 time.sleep(0.01)
