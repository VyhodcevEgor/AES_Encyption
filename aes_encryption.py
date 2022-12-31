import pyAesCrypt


def encrypt_data():
    password = input('Enter the password: ')
    pyAesCrypt.encryptFile('text.txt', 'encrypted_text.aes', password)


def decrypt_data():
    password = input('Enter the password: ')
    pyAesCrypt.decryptFile(
        'encrypted_text.aes', 'decrypted_text.txt', password
    )


if __name__ == '__main__':
    # encrypt_data()
    decrypt_data()
