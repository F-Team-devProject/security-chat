
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import serilization
from cryptography.hazmat.primitives.asymmetric import hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key= rsa.generate_private_key(public_exponenet=65537,key_size=2048)
public_key= private_key.public_key()

message= b"a secret message"
encryption= pubic_key.encrypt(message,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
