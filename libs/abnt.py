import utils.print as serialPrint
from crccheck.crc import Crc16Arc
from time import sleep


def send(ser, cmd, args = None):
    """Monta frame de envio, calculando CRC16 do packet e imprimindo-o no terminal.
        
    Parameters: 
    ser (str): Porta COM
    cmd (str): Octeto identificador do comando
    args (str): Octetos adicionais de interesse
    
    Returns: None 
    """
    # Limpa porta
    packet = bytearray()
    packet.append(cmd)
    if (args is not None):
        for i in args:
            packet.append(i)
    while (len(packet) < 64):
        packet.append(0x0)
    crc = Crc16Arc.calc(packet)    
    packet.append(crc%256)
    packet.append(crc//256)
    
    ser.flush()    
    while ser.inWaiting()<3:
        sleep(0.0001)
    ser.read(ser.inWaiting())
    ser.write(packet)
    serialPrint.TxprintHex(packet)
    
def read(ser, cmd, timeOut=2):
    Flag = False
    validCommand = False
    packet = bytearray()
    syncCount = 0
    sleep(timeOut)
    while len(packet) < 258 and ser.inWaiting() > 0 and syncCount < 3:
        b = ord(ser.read(1))
        if not validCommand and b!= 0xFF and b!=0x05:
            validCommand = True
        if not validCommand and b== 0x05:
            syncCount+=1
        if validCommand:
            packet.append(b)
    serialPrint.RxprintHex(packet, end=" >> ")    
    if len(packet) < 258:
        serialPrint.error("Resposta Inválida")
    else:
        crc = packet[256] + 256*packet[257]
        if packet[0] != cmd:
            serialPrint.error('Resposta inesperada')
        elif crc!= Crc16Arc.calc(packet[0:256]):
            serialPrint.error('CRC inválido')
        else: 
            serialPrint.info('Comando OK')
            Flag=True
    returnData = dict()
    returnData['data'] = packet
    returnData['flag'] = Flag
    return returnData
    
