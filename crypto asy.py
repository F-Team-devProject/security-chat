from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

"""private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

private_key_pem = private_key.private_bytes( #convert key to text format
    encoding=serialization.Encoding.PEM,
    format = serialization.PrivateFormat.PKCS8,
    encryption_algorithm = serialization.NoEncryption() #does not encrypt the file
)
with open("private_key.pem", "wb") as file: #creat a file private_key.pem,wb=write in byte
    file.write(private_key_pem)   
    

public_key_pem = public_key.public_bytes( #convert key to text format
    encoding=serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo,
)
with open("public_key.pem", "wb") as file: #creat a file private_key.pem,wb=write in byte
    file.write(public_key_pem) """     

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
