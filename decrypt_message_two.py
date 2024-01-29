encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
decrypted_message = ""

# flip every other letter with its cooresponding letter  from the end of the string
for i in range(0, len(encrypted_message)-1, 2):
    decrypted_message += encrypted_message[i]
    decrypted_message += encrypted_message[-i-2]

# Print result
print(decrypted_message)


