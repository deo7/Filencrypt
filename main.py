#     _____               ____          _____             
#    |  __ \             |  _ \        |  __ \            
#    | |  | | _____   __ | |_) |_   _  | |  | | ___  ___  
#    | |  | |/ _ \ \ / / |  _ <| | | | | |  | |/ _ \/ _ \ 
#    | |__| |  __/\ V /  | |_) | |_| | | |__| |  __/ (_) |
#    |_____/ \___| \_/   |____/ \__, | |_____/ \___|\___/ 
#                                __/ |                    
#                               |___/                     


from hashlib import sha256
import pyfiglet
import random
import string
import time
import sys

ascii_banner = pyfiglet.figlet_format("CryptMyFile")
print(ascii_banner)
symbol = chr(9829)
print("Made with " + symbol + " by Déodorant")

time.sleep(1)

print("====================")
language_choice = input("Select your language please:\n\n[1] Français\n[2] English\n\n    Choice: ")

language_choice_fr = ["1", "fr", "french", "français"]
language_choice_en = ["2", "en", "english", "anglais"]

if language_choice in language_choice_fr:
    print("====================")

    menu_choice = input("Menu d'interaction:\n\n[1] Chiffrer un fichier\n[2] Déchiffrer un fichier\n[3] Page d'aide\n\n    Choix: ")

    encrypt_list_fr = ["1", "chiffrer", "chiffrer un fichier"]
    decrypt_list_fr = ["2", "déchiffrer", "déchiffrer un fichier"]
    help_list_fr = ["3", "aide", "page d'aide"]

    if menu_choice in encrypt_list_fr:
        print("====================")

        start_file = input("Quel est le nom du fichier à chiffrer (avec l'extension) ?  ")

        try:
            with open(start_file, 'r'):
                pass
        except IOError: 
            sys.exit("Fichier introuvable (vérifiez que le fichier à chiffrer est dans le même dossier que ce fichier - main.py)")
        
        end_file = input("Quel nom voulez-vous donner au fichier final (=le fichier chiffré) ?  ")

        if end_file == "":
            end_file = "crypt_" + str(start_file)

        def getKey(length):
            str = string.ascii_letters + string.digits
            return "".join(random.choice(str) for i in range(length))

        key = getKey(3000)
        key_file = "key.txt"

        with open(key_file, 'w') as kf:
            kf.write(key)
            
        print("====================")
        print("Chiffrement en cours...")

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

                time.sleep(2)

                print("====================")
                print("Chiffrement terminé!")
                time.sleep(1)
                print("====================")
                print("Le fichier: " + str(start_file) + " est maintenant chiffré dans le fichier: " + str(end_file))
                time.sleep(1)
                print("====================")
                print("De plus, un fichier 'key.txt' contanant votre clé de chiffrement a été crée, celle-ci fait 3000 caractères et elle vous servira si vous souhaitez déchiffrer votre fichier par la suite")


    elif menu_choice in decrypt_list_fr:
        print("====================")

        decrypt_start_file = input("Quel est le nom du fichier à déchiffrer (avec l'extension) ?  ")

        try:
            with open(decrypt_start_file, 'r'):
                pass
        except IOError: 
            sys.exit("Fichier introuvable (vérifiez que le fichier à déchiffrer est dans le même dossier que ce fichier - main.py)")


        decrypt_end_file = input("Quel nom voulez-vous donner au fichier final (=fichier déchiffré)?  ")

        if decrypt_end_file == "":
            decrypt_end_file = "decrypt_" + str(decrypt_start_file)

        encryption_key = input("Quelle est la clé de chiffrement utilisée lors du chiffrement de ce fichier (celle-ci est normalement dans 'key.txt') ?  ")
        len_encryption_key = len(encryption_key)

        if len_encryption_key != 3000:
            sys.exit("La clé de chiffrement n'est pas correcte, celle-ci devrait faire 3000 caractères et elle en fait: " + str(len_encryption_key))

        else:

            print("====================")
            print("Déchiffrement en cours...")

            key_encrypted = sha256(encryption_key.encode('utf-8')).digest()
            with open(decrypt_start_file, 'rb') as f_start_file:
                with open(decrypt_end_file, 'wb') as f_end_file:
                    i = 0
                    while f_start_file.peek():
                        c = ord(f_start_file.read(1))
                        j = i % len(key_encrypted)
                        b = bytes([c^key_encrypted[j]])
                        f_end_file.write(b)
                        i = i + 1

                    time.sleep(2)

                    print("====================")
                    print("Déchiffrement terminé!")
                    time.sleep(1)
                    print("====================")
                    print("Le fichier: " + str(decrypt_start_file) + " est maintenant déchiffré dans le fichier: " + str(decrypt_end_file))

    elif menu_choice in help_list_fr:
        print("====================")
        print("Page d'aide de CryptMyFile\n\nPrésentation\nCryptMyFile chiffre et déchiffre vos fichiers en XOR avec une clé de chiffrement générée de 3000 caractères qui est par la suite hashée en sha256 (donc tkt c'est safe). Vous pouvez normalement (dé)chiffrer des fichiers de tous types (txt, png, js...)\n\nConseils\nSi vous voulez déchiffrer un fichier, veillez à utiliser la même clé utilisée pour le chiffrement de ce fichier (voir 'key.txt'). Pour que le (dé)chiffrement fonctionne vous devez mettre ce fichier (main.py) dans le même dossier que le fichier à (dé)chiffrer\n\nContact\nDevByDeo - deodev@protonmail.com")

    else:
        print("====================")
        sys.exit("Vous devez répondre par '1', '2' ou '3'")

elif language_choice in language_choice_en:
    print("====================")
    
    menu_choice = input("Interaction menu:\n\n[1] Encrypt a file\n[2] Decrypt a file\n[3] Help page\n\n    Choice: ")

    encrypt_list_en = ["1", "encrypt", "encrypt a file"]
    decrypt_list_en = ["2", "decrypt", "decrypt a file"]
    help_list_en = ["3", "help", "help page"]

    if menu_choice in encrypt_list_en:
        print("====================")

        start_file = input("What's the name of the file to encrypt (with extension) ?  ")

        try:
            with open(start_file, 'r'):
                pass
        except IOError: 
            sys.exit("File not found (verify that the file to be encrypted is in the same folder as this file - main.py)")

        end_file = input("What name do you want to give to the final file (=encrypted file) ?  ")

        if end_file == "":
            end_file = "crypt_" + str(start_file)

        def getKey(length):
            str = string.ascii_letters + string.digits
            return "".join(random.choice(str) for i in range(length))

        key = getKey(3000)
        key_file = "key.txt"

        with open(key_file, 'w') as kf:
            kf.write(key)

        print("====================")
        print("Encryption in progress...")

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

                time.sleep(2)

                print("====================")
                print("Encryption complete!")
                time.sleep(1)
                print("====================")
                print("The file: " + str(start_file) + " is now encrypted in the file: " + str(end_file))
                time.sleep(1)
                print("====================")
                print("Then, a 'key.txt' file containing your encryption key has been created. Encryption key is 3000 characters long and you will use it to decrypt your file later")


    elif menu_choice in decrypt_list_en:
        print("====================")

        decrypt_start_file = input("What's the name of the file to decrypt (with extension) ?  ")

        try:
            with open(decrypt_start_file, 'r'):
                pass
        except IOError: 
            sys.exit("File not found (verify that the file to be decrypted is in the same folder as this file - main.py)")


        decrypt_end_file = input("What name do you want to give to the final file (=decrypted file) ?  ")

        if decrypt_end_file == "":
            decrypt_end_file = "decrypt_" + str(decrypt_start_file)

        encryption_key = input("What's the encryption key used when encrypting this file (this is normally in 'key.txt')?  ")
        len_encryption_key = len(encryption_key)

        if len_encryption_key != 3000:
            sys.exit("Encryption key is incorrect, it should be 3000 characters long but it contains: " + str(len_encryption_key) + " characters long")

        else:

            print("====================")
            print("Decryption in progress...")

            key_encrypted = sha256(encryption_key.encode('utf-8')).digest()
            with open(decrypt_start_file, 'rb') as f_start_file:
                with open(decrypt_end_file, 'wb') as f_end_file:
                    i = 0
                    while f_start_file.peek():
                        c = ord(f_start_file.read(1))
                        j = i % len(key_encrypted)
                        b = bytes([c^key_encrypted[j]])
                        f_end_file.write(b)
                        i = i + 1

                    time.sleep(2)

                    print("====================")
                    print("Decryption complete!")
                    time.sleep(1)
                    print("====================")
                    print("The file: " + str(decrypt_start_file) + " is now decrypted in the file: " + str(decrypt_end_file))

    elif menu_choice in help_list_en:
        sys.exit("Help page only exist in french for the moment")

    else:
        print("====================")
        sys.exit("You must reply by '1', '2' or '3'")

else:
    print("====================")
    sys.exit("You must reply by '1' or '2'")







#         _                _                                   _                              _ _                      
#        | |              | |            ____                 | |                            (_) |                     
#      __| | ___  ___   __| | _____   __/ __ \ _ __  _ __ ___ | |_ ___  _ __  _ __ ___   __ _ _| |  ___ ___  _ __ ___  
#     / _` |/ _ \/ _ \ / _` |/ _ \ \ / / / _` | '_ \| '__/ _ \| __/ _ \| '_ \| '_ ` _ \ / _` | | | / __/ _ \| '_ ` _ \ 
#    | (_| |  __/ (_) | (_| |  __/\ V / | (_| | |_) | | | (_) | |_ (_) | | | | | | | | | (_| | | |_ (__ (_) | | | | | |
#     \__,_|\___|\___/ \__,_|\___| \_/ \ \__,_| .__/|_|  \___/ \__\___/|_| |_|_| |_| |_|\__,_|_|_(_)___\___/|_| |_| |_|
#                                       \____/| |                                                                      
#                                             |_|                                                                      
