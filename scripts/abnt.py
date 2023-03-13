import libs.abnt as abnt
import serial
from utils.print import *
from utils.conv import *
def run(port):
    ser = serial.Serial(port)
    h1("Teste do protocolo ABNT")
    h2("Comando 0x81")
    abnt.send(ser, 0x81)
    ans = abnt.read(ser, 0x81)['data']
    serialNumber = ans[1:5]
    print(bin2HexStr(serialNumber))