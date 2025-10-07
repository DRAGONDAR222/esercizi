# modulus

n_str = """     
00:b4:b3:b4:51:0d:d5:df:d8:94:3f:46:19:e7:50:
ef:54:75:a6:ef:df:34:a5:bd:55:bc:c1:50:f8:39:
3c:a6:d6:87:d7:87:16:cd:19:13:32:73:99:e9:b7:
8c:8c:3c:10:52:98:e3:7b:5c:0d:c8:8f:ad:45:ee:
7f:f6:6f:04:c4:df:d5:6c:49:1a:4b:05:5d:75:b8:
cf:c6:1b:b0:36:a1:2e:bf:fe:1c:21:b7:cd:37:49:
83:80:23:9e:df:9e:cb:9c:59:47:3d:9b:f6:42:1c:
ee:56:4f:d9:e1:1c:b8:b6:bf:47:7e:a3:a2:ed:b4:
c6:46:b5:01:14:d6:63:44:91:40:63:87:5c:a3:86:
e2:16:a8:54:c1:85:66:40:49:9f:27:29:f1:99:14:
5d:18:0b:4b:17:7e:3c:cb:c0:20:01:99:11:ad:4d:
dc:dc:1b:87:1c:f6:fd:d3:bd:86:6f:6b:14:e2:9a:
e4:15:41:f2:9b:a4:5d:57:ec:50:25:bf:69:77:55:
66:4b:38:ae:6f:82:72:5d:23:03:c1:f4:93:0b:03:
50:0c:74:0b:2e:0f:4a:e5:3d:72:1a:41:6c:f6:d2:
62:2d:08:0d:43:08:c3:b9:c3:18:7b:a3:e5:56:10:
c4:e4:d7:9b:a7:56:bc:b6:61:68:44:8d:d6:e9:56:
9b:a1
"""

# private exponent

d_str = """
1e:1d:f3:62:d7:a3:a5:4e:c3:5f:e1:04:51:38:27:
e3:68:f1:27:fa:88:c6:4a:38:f4:ca:e2:d4:09:8a:
1b:ce:6b:f9:41:2e:77:84:2d:dd:bd:ee:fc:49:42:
17:5f:58:0d:c4:25:e9:e4:ac:f6:c2:9c:e0:fd:15:
53:bd:2b:76:25:4e:3c:b6:d9:b7:2b:8f:93:9e:cd:
4b:af:48:09:1a:dd:1f:ff:af:5a:f3:f7:89:36:eb:
40:05:ef:cf:ef:cc:9a:0e:e1:34:ef:53:b5:af:7d:
0e:62:a4:50:2f:74:1e:75:36:95:1b:45:d2:48:cb:
b6:73:80:2e:23:bb:36:17:ed:96:69:6d:a3:0d:3f:
ca:92:55:fe:ed:73:19:be:43:78:57:59:3e:c2:b7:
bf:51:19:be:dc:0e:f6:25:99:8a:34:ec:c1:f7:03:
b1:eb:4a:5c:1d:ec:7a:64:aa:48:6f:a5:92:f0:34:
46:21:ec:d7:ca:c0:db:8b:2e:a9:fc:5c:71:f0:2c:
3c:76:c4:7b:9e:66:d1:db:cc:ef:a6:1f:25:f7:a3:
9e:1d:e8:91:16:9b:69:8a:d0:4d:de:06:d1:26:6e:
65:7d:c7:de:f6:88:1d:ff:b4:af:ec:1c:54:3c:5e:
42:9a:7a:2c:6c:20:71:a1:87:48:e5:6c:d6:dc:52:
59
"""



# public exponent

e = 3 # lo leggo dal terminale


n = ''.join([x for x in n_str if x.isalnum()])
d = ''.join([x for x in d_str if x.isalnum()])

n = int(n,16)
d = int(d,16)


def Cifra(M,e,n):
    return pow(M,e,n)


def Decifra(C,d,n):
    return pow(C,d,n)



msg = "Ciao"
print("\nMessaggio originale:", msg)

# Converti messaggio -> intero

M = int.from_bytes(msg.encode("utf-8"), "big")
print("Messaggio come intero:", M)


C = Cifra(M, e, n)

print("Cifrato:", C)


M2 = Decifra(C, d, n)
M2_bytes = M2.to_bytes((M2.bit_length() + 7) // 8, "big")

print("Decifrato:", M2_bytes.decode("utf-8"))