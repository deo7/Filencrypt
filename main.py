#     _____               ____          _____             
#    |  __ \             |  _ \        |  __ \            
#    | |  | | _____   __ | |_) |_   _  | |  | | ___  ___  
#    | |  | |/ _ \ \ / / |  _ <| | | | | |  | |/ _ \/ _ \ 
#    | |__| |  __/\ V /  | |_) | |_| | | |__| |  __/ (_) |
#    |_____/ \___| \_/   |____/ \__, | |_____/ \___|\___/ 
#                                __/ |                    
#                               |___/                     


from hashlib import sha256
import random
import string
import pyfiglet
import time


ascii_banner = pyfiglet.figlet_format('CryptMyFile')
print(ascii_banner)

time.sleep(2)

choice = input('Menu d\'interaction:\n\n[1] chiffrer un fichier\n[2] déchiffrer un fichier\n[3] page d\'aide\n\n    Choix: ')

if choice == '1':
    print('====================')
    start_file = input('Quel est le nom du fichier à chiffrer (avec l\'extension)?  ')
    end_file = input('Choisissez le nom du fichier final (=fichier chiffré)?  ')
    key = input('Entrer la clé de chiffrement de votre choix (ou faites "gen" pour en générer une):  ')

    if key == 'gen':
        def getCryptKey(length):
            str = string.ascii_letters
            return ''.join(random.choice(str) for i in range(length))

        cryptkey = getCryptKey(12)

        print('====================')
        print('Voici la clé de chiffrement: ' + cryptkey + '\nVeillez à garder cette clé de chiffrement, elle vous servira si vous voulez déchiffrer votre fichier par la suite')

        time.sleep(3)

        key_encrypted = sha256(cryptkey.encode('utf_8')).digest()
        with open(start_file, 'rb') as f_start_file:
            with open(end_file, 'wb') as f_end_file:
                i = 0
                while f_start_file.peek():
                    c = ord(f_start_file.read(1))
                    j = i % len(key_encrypted)
                    b = bytes([c^key_encrypted[j]])
                    f_end_file.write(b)
                    i = i + 1
                print('====================')
                print('Le fichier: ' + str(start_file) + ' est maintenant chiffré dans: ' + str(end_file) + '\nN\'oubliez pas la clé de chiffrement que vous avez générée: ' + cryptkey)
                print('====================')
                print('DevByDeo - deodev@protonmail.com')

    else:
        key_encrypted = sha256(key.encode('utf-8')).digest()
        with open(start_file, 'rb') as f_start_file:
            with open(end_file, 'wb') as f_end_file:
                i = 0
                while f_start_file.peek():
                    c = ord(f_start_file.read(1))
                    j = i % len(key_encrypted)
                    b = bytes([c^key_encrypted[j]])
                    f_end_file.write(b)
                    i = i + 1
                print('====================')
                print('Le fichier: ' + str(start_file) + ' est maintenant chiffré dans: ' + str(end_file))
                print('====================')
                print('DevByDeo - deodev@protonmail.com')

elif choice == '2':
    print('====================')
    start_file = input('Quel est le nom du fichier à déchiffrer (avec l\'extension)?  ')
    end_file = input('Choisissez le nom du fichier final (=fichier déchiffré)?  ')
    key = input('Entrer la clé de chiffrement utilisée pour chiffrer le fichier:  ')

    key_encrypted = sha256(key.encode('utf-8')).digest()
    with open(start_file, 'rb') as f_start_file:
        with open(end_file, 'wb') as f_end_file:
            i = 0
            while f_start_file.peek():
                c = ord(f_start_file.read(1))
                j = i % len(key_encrypted)
                b = bytes([c^key_encrypted[j]])
                f_end_file.write(b)
                i = i + 1
            print('====================')
            print('Le fichier: ' + str(start_file) + ' est maintenant déchiffré dans: ' + str(end_file))
            print('====================')
            print('DevByDeo - deodev@protonmail.com')

elif choice == '3':
    print('====================')
    print('Page d\'aide de CryptMyFile\n\nCryptMyFile chiffre et déchiffre vos fichiers en XOR avec la clé de chiffrement de votre choix ou une clé de chiffrement générée (qui est par la suite hashée en sha256)\nVous pouvez (dé)chiffrer des fichiers de tout types (txt, png, js...) mais il est possible que certaines extensions ne soient pas (dé)chiffrable\nSi vous voulez déchiffrer un fichier, veillez à utiliser la même clé utilisée pour le chiffrement de ce fichier\nPour que le (dé)chiffrement fonctionne vous devez mettre ce fichier (main.py) dans le même dossier que le fichier à (dé)chiffrer\n\nCodé par Déodorant\ndeodev@protonmail.com')
            

else:
    print('====================')
    print('Vous devez répondre obligatoirement par "1", "2" ou "3"')
    print('====================')
    print('DevByDeo - deodev@protonmail.com')



#         _                _                                   _                              _ _                      
#        | |              | |            ____                 | |                            (_) |                     
#      __| | ___  ___   __| | _____   __/ __ \ _ __  _ __ ___ | |_ ___  _ __  _ __ ___   __ _ _| |  ___ ___  _ __ ___  
#     / _` |/ _ \/ _ \ / _` |/ _ \ \ / / / _` | '_ \| '__/ _ \| __/ _ \| '_ \| '_ ` _ \ / _` | | | / __/ _ \| '_ ` _ \ 
#    | (_| |  __/ (_) | (_| |  __/\ V / | (_| | |_) | | | (_) | |_ (_) | | | | | | | | | (_| | | |_ (__ (_) | | | | | |
#     \__,_|\___|\___/ \__,_|\___| \_/ \ \__,_| .__/|_|  \___/ \__\___/|_| |_|_| |_| |_|\__,_|_|_(_)___\___/|_| |_| |_|
#                                       \____/| |                                                                      
#                                             |_|                                                                      