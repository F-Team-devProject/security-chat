from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("private_key.pem", "rb") as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None,
        backend= default_backend()
    )
with open("public_key.pem", "rb") as file:
    public_key = serialization.load_pem_public_key(
        file.read(),
        backend= default_backend()
    ) 
message = input("Insert message > ").encode()

encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA1()),
       algorithm=hashes.SHA1(),
       label=None 
    )
) 

print(f"Encrypted : {encrypted_message}")

decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
       mgf=padding.MGF1(algorithm=hashes.SHA1()),
       algorithm=hashes.SHA1(),
       label=None 
    )
) 

print(f"Decrypted : {decrypted_message}")     
