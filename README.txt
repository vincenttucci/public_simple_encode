This code is a simple program that represents the initial step in our old encryption software, and
simply is used for converting final stage passwords.

The program works as follows:

1. The user enters the character "e" or "d" to tell
the program that they want to encrypt/decrypt the 
text. If the user enters anything else, the program
returns an error.



2. If the user inputs "d", they are asked to input the
encrypted text, and then an integer representing the unquie 
hash value for their decryption. The program then returns
the decrypted text.

If the user inputs "e", they are then asked to input a 
string that will be encrypted by the program. The program 
will return an encrypted string value and a hash number, and it
is important that the user remeber's this value along with the text.

***Note that each time a string is inputed, the program
will always return the same hash value.




