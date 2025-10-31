import random

def xor_cipher(Texto):
    clave = ''.join(random.choice('01') for _ in Texto)
    encriptacion = ''.join(chr(ord(Texto[i]) ^ int(clave[i])) for i in range(len(Texto)))
    desencriptar = ''.join(chr(ord(encriptacion[i]) ^ int(clave[i])) for i in range(len(encriptacion)))
    return clave, encriptacion, desencriptar

if __name__ == "__main__":
    text = input("Texto a encriptar: ")
    clave, encriptacion, desencriptar = xor_cipher(text)
    print(f"CLave: {clave}")
    print(f" Texto encriptado: {encriptacion}")
    print(f"Texto desencriptar: {desencriptar} ")