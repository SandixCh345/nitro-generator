import random
import string
from colorama import Fore

def nitro():
    for i in range (500):
        random_source = string.ascii_letters
        rtn=random.choice(string.ascii_lowercase)
        rtn += random.choice(string.ascii_uppercase)

        for i in range(14):
            rtn +=random.choice(random_source)
        rtn_list = list(rtn)
        random.SystemRandom().random.shuffle(rtn_list)
        rtn ='' .join (rtn_list)

        print(Fore.RED + "[INFO]" +Fore.GREEN + F'https//discord.gift/{rtn}')  
        

