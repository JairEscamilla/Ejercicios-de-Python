# Se tiene que instalar crypto con pip install crypto
import Crypto
import binascii
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
random_generator = Crypto.Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

print private_key
print public_key

private_key = private_key.exportKey(format = 'DER')
public_key = public_key.exportKey(format = 'DER')

private_key = binascii.hexlify(private_key).decode('utf8')
public_key = binascii.hexlify(public_key).decode('utf8')

print "Clave privada: ", private_key
print "Clave publica: ", public_key

# Conversion de ascci a llave privada
# private_key = RSA.importKey(binascii.unhexlify(private_key))
# public_key = private_key.publickey()

# Conversion de ascci a llave publica
# public_key = RSA.importKey(binascii.unhexlify(public_key))
