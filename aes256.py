
class AES256():
    """ AES256-CBC encryption/decryption implementation """

    import pyAesCrypt

    def __init__(self, bufferSize=512*1024):
        """ Buffer memory size in bytes (default: 512*1024) """

        self.bufferSize = bufferSize

    def crypt(self, dir):
        """ Crypts file with AES256-CBC. dir - str: file name (e.g.: test.txt) """

        print('-----------------------------------')
        password = input('Enter key: ')

        pyAesCrypt.encryptFile(str(dir), str(dir)+'.aes',
                               password, self.bufferSize)
        print('[Crypted] ' + str(dir) + '.aes')

    def decrypt(self, dir):
        """ Decrypts file with AES256-CBC. dir - str: file name (e.g.: test.txt) """

        try:
            print('-----------------------------------')
            password = input('Enter key: ')
            pyAesCrypt.decryptFile(
                str(dir) + '.aes', 'decrypted.' + str(dir), password, self.bufferSize)
            print('[Decrypted] decrypted.' + str(dir))
        except:
            print('Error! Wrong key!')
