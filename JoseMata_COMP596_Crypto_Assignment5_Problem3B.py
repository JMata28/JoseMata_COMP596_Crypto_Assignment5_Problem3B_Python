#This is José Mata's submission for Question #3b of Assignment 5 of the class COMP 596 - Cryptography
#Explanations and examples of Python from the linked ChatGPT log were used to put together this code: https://chat.openai.com/share/1fd41438-0d7b-4610-8e18-89ac3f5c82b9

#The store_message function stores the message in an array separating the characters in groups of two and as hex values
def store_message(message):
    m = list()
    for i in range(len(message)):
        if i%2 == 0: #For only the even indexes
            block = message[i]+message[i+1] #Concatenate the character in the index and the next character
            hex_block = int(block, 16) #Turn the characters into a HEX value
            m.append(hex_block) #Append to the list "m"
    return m

#The encryption_box function implements the encryption function E as described by the instructions for Problem 3
def encryption_box(m, h):
     if h == 1 or h == 0:
        encrypted_output = int("D", 16)
        return encrypted_output
     else:
        encrypted_output = m % h
        return encrypted_output

#The XOR function is a simple bitwise XOR operation between two inputs        
def XOR(encrypted_output, h):
    compression_function_output = encrypted_output^h
    return compression_function_output

message = input("Welcome to José Mata's ByteHA hash algorithm program.\nPlease enter your HEX message:\n")
IV = input("Please enter your initialization vector (IV):\n")
IV_hex = int(IV, 16) #Save the IV as a hex value
m = store_message(message) 

#Run the compression function for each block of the message. If it is the first block, h = IV. For the subsequent blocks, h is the output of the previous compression function. 
for i in range(len(m)):
    if i ==0:
        encrypted_output = encryption_box(m[i], IV_hex)
        compression_function_output = XOR(encrypted_output, IV_hex)
    else:
        encrypted_output = encryption_box(m[i], compression_function_output)
        compression_function_output = XOR(encrypted_output, compression_function_output)

print("Your message is: ", message, "\n")
print("Your initialization vector is: ", hex(IV_hex), "\n")
print("H(m) is: ", hex(compression_function_output))



