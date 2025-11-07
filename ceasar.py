def message_to_binary(message):
    binary_string = ''.join(format(ord(c), '08b') for c in message) #convert words to binary
    return binary_string 
b = input("enter a message:")
binary_string = message_to_binary(b) # nb: to have a message as 'label' in binary, each letter was xor'd with binary_value

c = int(input("enter a number:")) #convert integer to binary
binary_value = bin(c)

bin_num1 = binary_string   
bin_num2 = binary_value

def binary_xor(bin_num1 , bin_num2):
    
    int_num1 = int(bin_num1, 2)
    int_num2 = int(bin_num2, 2)
    
    
    xor_result = int_num1 ^ int_num2 #xor of the two results
    

    bin_result = bin(xor_result)[2:]
    
    return bin_result
binary_s = binary_xor(bin_num1, bin_num2)

def binary_to_message(binary_string):
    """
    Converts a binary string 
    into a human-readable message.
    """
    padding = len(binary_string) % 8 
    if padding !=0:
        binary_string = '0' * (8 - padding) + binary_string #if the binary digit is not a multiple of 8,Zero's is being completed infront 
    message_chars = []
    for i in range(0, len(binary_string), 8):
        byte_binary = binary_string[i:i+8]
        decimal_value = int(byte_binary, 2)  # Convert binary to integer
        character = chr(decimal_value)      # Convert integer to character
        message_chars.append(character)

    return "".join(message_chars)

a = binary_s 
decoded_message = binary_to_message(a)
print(f"The binary string: {a}")
print(f"The decoded message: {decoded_message}")


          
       

