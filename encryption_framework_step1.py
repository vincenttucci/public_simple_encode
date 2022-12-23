from bakery import assert_equal

def encrypt_text(message: str, rotation_amount: int) -> str:
    '''
    Consumes the plaintext message (a string) and rotation_amount (an integer) 
    and produces a string where the text is encrypted as follows:
    
    1. Converts the string to a list of integers using ord.
    2. Rotates each integer of the string by rotation_amount amount using the 
       following formula: rotated = (original+rotation-32) % 94 + 32.
    3. Inserts the tilde ASCII value (126, which translates to "~") after every integer less than 48.
    4. Converts the list of integers back to a string using chr
    '''
    
    numbers = []
    for character in message:
        numbers.append(ord(character))
        
    new_list = []
    for number in numbers:
        rotated = (number + rotation_amount - 32) % 94 + 32
        new_list.append(rotated)
        if rotation_amount < 48:
            new_list.append(126)
    
    secret_string = ''
    for item in new_list:
        secret_string += chr(item)
    return secret_string
    
def decrypt_text(message: str, rotation_amount: int) -> str:
    '''
    Consumes the encrypted message (a string) and rotation_amount (an integer) 
    and produces a string where the text is decrypted as follows:

    1. Converts the string to a list of integers using ord.
    2. Filters the list to remove any occurrence of the value 126 (the tilde "~").
    3. The integers in the list are rotated -rotation_amount amount.
    4. Converts the list of integers back to a string using chr.
    '''
    number_list = []
    for character in message:
        changed = ord(character)
        if changed != 126:
            rotated = (changed - rotation_amount - 32) % 94 + 32
            number_list.append(rotated)
    new_message = ''
    for number in number_list:
        new_message += chr(number)
    return new_message
    
assert_equal(encrypt_text('hello', 2), 'j~g~n~n~q~')
assert_equal(encrypt_text("Dr. Bart", 20), 'X~(~B~4~V~u~(~*~')
assert_equal(encrypt_text('goodbye', 900), '?GG<:Q=')
                                              
assert_equal(decrypt_text('j~g~n~n~q~', 2), 'hello')
assert_equal(decrypt_text("X~(~B~4~V~u~(~*~", 20), 'Dr. Bart')
assert_equal(decrypt_text('?GG<:Q=', 900), 'goodbye')

def hash_text (message: str, base: int, hash_size: int) -> int:
    '''
    consume a string (any kind of message) and two 
    integers (base and hash_size), and produces an 
    integer that attempts to uniquely represent the text.
    '''
    ints = []
    for char in message:
        ints.append(ord(char))
        
    count = 0
    new_ints = [] 
    for num in ints:
        new_ints.append((count + base) ** num)
        count += 1
    
    new_nums = sum(new_ints)
    return new_nums % hash_size
   
assert_equal(hash_text('hi', 1, 2), 1)
assert_equal(hash_text('hi', 1, 200), 33)
assert_equal(hash_text('delta', 0, 3000),2562)

def main():
    '''
    The main function works as follows:

    1. The user is prompted to input their desired action.
        2. If the user enters encrypt, they then enter a message.
        3. The encrypted message is returned along with
           a hash value to be used in decrypting it.
                                OR
        2. If the user enters decrypt, they then enter a message and expected hash value.
        3. The hash of the decrypted message is compared to the expected hash.
        4. If the hashes are the same, print the decrypted message.
        5. If the hashes are different, return an error message
    '''
    enc_dec = input('Type "e" to encrypt or "d" to decrypt: ')
    
    if enc_dec == 'e':
        message = input('Enter your text: ')
        encrypted =(encrypt_text(message, 18))
        print (encrypted)
        print ('Your hash value is: ' + str(hash_text(encrypted, 1000000000, 31)))
    elif enc_dec == 'd':
        message = input('Enter your text: ')
        expected_hash = int(input('Enter the expected hash:  '))
        if expected_hash == hash_text(message, 1000000000, 31):
            decrypted = decrypt_text(message, 18)
            print ('the decrypted message is: ' + decrypted)
        else:
            print('ERROR')
    else:
        print ('ERROR')
            
main()