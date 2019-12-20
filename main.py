# AES256-CBC implementation

import aes256


# bufferSize = 512*1024

aes = aes256.AES256()

flag = True
while flag:
    print('-----------------------------------')
    action = input(
        'Select an option (1 - crypt a file, 2 - decrypt a file, 3 - exit): ')

    if action == '1':
        dir = input('Enter file name: ')
        aes.crypt(dir)
    elif action == '2':
        dir = input('Enter file name: ')
        aes.decrypt(dir)
    elif action == '3':
        flag = False
        exit()
    else:
        print('Wrong action! Try again!')
