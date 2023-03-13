from colorama import Fore
from colorama import Back
from colorama import Style
    
def TxprintHex(packet):
    print (Fore.CYAN + 'Tx: [%s]' % ' '.join('{:02X}'.format(x) for x in packet) + Style.RESET_ALL)
    
def RxprintHex(packet, end="\n"):
    print (Fore.RED + 'Rx: [%s]' % ' '.join('{:02X}'.format(x) for x in packet) + Style.RESET_ALL, end=end)
    
def h1(str):
    print(f'{Back.GREEN}{Fore.WHITE}{str}{Style.RESET_ALL}\n')

def h2(str):
    print(f'{Fore.GREEN}{str}{Style.RESET_ALL}')
    
def info(str):
    print(f'{Fore.GREEN}{str}{Style.RESET_ALL}\n')
    
def error(str):
    print(f'{Fore.YELLOW}{str}{Style.RESET_ALL}\n')