c1 = input("Enter a hex_string:")
c2 = input("Enter a second hex_string:")
a = bytes.fromhex(c1)   #convert from hex to byte
b = bytes.fromhex(c2)

bytes_data1 = a
bytes_data2 = b

def bytes_to_binary(bytes_data1 , bytes_data2):
    
    decimal_value1 = int.from_bytes(bytes_data1,byteorder='big')    #convert from bytes to binary
    decimal_value2 = int.from_bytes(bytes_data1,byteorder='big')
    binary_string1 = bin(decimal_value1)[2:].zfill(len(bytes_data1)*8)        #[2:] use to remove the prefix 0b added by the fonction bin()
    binary_string2 = bin(decimal_value1)[2:].zfill(len(bytes_data2)*8)
    return [ binary_string1 , binary_string2 ]
BTB =  bytes_to_binary(bytes_data1 , bytes_data2)

a = BTB[0]
b = BTB[1]

print(BTB)
def xor_binaire(a,b):
    return ''.join('1' if x!=y else '0' for x,y in zip(a,b))   # zip pour iterer sur deux chaine de caractere en parallele et la comprehension de la liste pour effectuer le XOR sur chaque paire de bits
print( xor_binaire(a,b) )
binary =  xor_binaire(a,b)

def binary_to_hex(binary):
    return format(int(binary, 2), 'x')  # the 'x' is for result in small letter and 'X' for capital ones         
print(binary_to_hex(binary))