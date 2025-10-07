
# alternative alla codifica UTF-8 classica

def unicode_convert(msg:str) -> int:
    return int(''.join([str(ord(x)) for x in msg]))


def unicode_decript(msg_hashi:int) -> str:
    s = str(msg_hashi)      
    chars = [s[i:i+3] for i in range(0, len(s), 3)]
    return ''.join([chr(int(c)) for c in chars])


# codifica UTF-8 classica

def unicode_encode(msg: str) -> int:
    return int.from_bytes(msg.encode('utf-8'), 'big')

def unicode_decode(code: int) -> str:
    n_bytes = (code.bit_length() + 7) // 8
    return code.to_bytes(n_bytes, 'big').decode('utf-8')


# convertitore little endian
def s2n(s):
    tot = 0
    esp = 0

    for c in s:
        tot += 256**esp*ord(c)
        esp += 1

    return tot
    
# convertitore big endian
def s2ne(s):
    tot = 0

    for c in s:
        tot = (tot<<8)|ord(c)  # | or binario

    return tot
 

# algoritmo di diffie helman

