letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ''

    for letter in plaintext:
        letter = letter.upper()

        if letter == ' ':
            ciphertext += ' '
        else:
            index = letters.find(letter)

            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key

                if new_index >= num_letters:
                    new_index -= num_letters

                ciphertext += letters[new_index]

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ''

    for letter in ciphertext:
        letter = letter.upper()

        if letter == ' ':
            plaintext += ' '
        else:
            index = letters.find(letter)

            if index == -1:
                plaintext += letter
            else:
                new_index = index - key

                if new_index < 0:
                    new_index += num_letters

                plaintext += letters[new_index]

    return plaintext


print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('DO YOU WANT TO ENCRYPT OR DECRYPT?')
user_input = input('E/D: ').upper()
print()

if user_input == 'E':
    print('Encryption Mode Selected')
    print()

    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')

    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'D':
    print('Decryption Mode Selected')
    print()

    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')

    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
