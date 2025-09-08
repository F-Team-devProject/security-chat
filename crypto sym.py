from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"salut je m'appelle Melvine")
print("Encrypt: ", token)

d = f.decrypt(token)
print("decrypt: ", d)