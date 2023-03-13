def bin2HexStr(byteArray):
    return ' '.join('{:02X}'.format(x) for x in byteArray)
