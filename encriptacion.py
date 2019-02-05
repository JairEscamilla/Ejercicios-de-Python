from Crypto.Cipher import PKCS1_OAEP
message = "Hola mundo, esto es un mensaje en texto plano"
message = message.encode()

cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)
