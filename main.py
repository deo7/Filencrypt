#                    ,,,, 
#              ,;) .';;;;',
#  ;;,,_,-.-.,;;'_,|I\;;;/),,_
#   `';;/:|:);{ ;;;|| \;/ /;;;\__
#       L;/-';/ \;;\',/;\/;;;.') \
#       .:`''` - \;;'.__/;;;/  . _'-._ 
#     .'/   \     \;;;;;;/.'_7:.  '). \_
#   .''/     | '._ );}{;//.'    '-:  '.,L
# .'. /       \  ( |;;;/_/         \._./;\   _,
#  . /        |\ ( /;;/_/             ';;;\,;;_,
# . /         )__(/;;/_/                (;;'''''
#  /        _;:':;;;;:';-._             );
# /        /   \  `'`   --.'-._         \/
#        .'     '.  ,'         '-,
#       /    /   r--,..__       '.\
#     .'    '  .'        '--._     ]
#     (     :.(;>        _ .' '- ;/
#     |      /:;(    ,_.';(   __.'
#      '- -'"|;:/    (;;;;-'--'
#            |;/      ;;(
#            ''      /;;|
#                    \;;|
#                     \/

from hashlib import sha256
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyfiglet
import argparse
import random
import string
import time
import sys
import os
import colorama
from colorama import Fore, Style
from colorama.initialise import reset_all

def banner():
    pfbanner = pyfiglet.figlet_format("Filencrypt")
    print(pfbanner)
    print("[>] Made with", Fore.RED, chr(9829), Style.RESET_ALL, "by Déodorant")
    print("[>] v3.0")
    print("[>] https://github.com/deo7/Filencrypt")
    print("[>] deodev@protonmail.com")

def menu():
    print("\nMenu")
    print("[1] Encrypt file")
    print("[2] Decrypt File")
    print("[3] Help page")
    print("[4] Contact dev")

def encryption():
        start_file = input("\nWhat's the name of the file to encrypt (with extension) ?  ")

        try:
            with open(start_file, 'r'):
                pass
        except IOError: 
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File not found (verify that the file to be encrypted is in the same folder as this file - main.py)")

        end_file = input("What name do you want to give to the final file (=encrypted file) ?  ")

        if end_file == "":
            end_file = "encrypted_" + str(start_file)
        else:
            pass

        def getKey(length):
            str = string.ascii_letters + string.digits
            return "".join(random.choice(str) for i in range(length))

        key = getKey(3000)
        key_file = "key.txt"

        with open(key_file, 'w') as kf:
            kf.write("-----BEGIN KEY BLOCK-----\n" + key + "\n-----END KEY BLOCK-----")

        print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Encryption in progress...")

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

                time.sleep(3)

                print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Encryption complete!")
                print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " The file: " + str(start_file) + " is now encrypted in the file: " + str(end_file))
                time.sleep(1)
                print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Then, a 'key.txt' file containing your encryption key has been created. Encryption key is 3000 characters long and you will use it to decrypt your file later")

def decryption():
        decrypt_file = input("\nWhat's the name of the file to decrypt (with extension) ?  ")

        try:
            with open(decrypt_file, 'r'):
                pass
        except IOError: 
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File not found (verify that the file to be decrypted is in the same folder as this file - main.py)")


        decrypted_file = input("What name do you want to give to the final file (=decrypted file) ?  ")

        if decrypted_file == "":
            decrypted_file = "decrypted_" + str(decrypt_file)

        encryption_key = input("What's the encryption key used when encrypting this file (this is normally in 'key.txt')?  ")
        len_encryption_key = len(encryption_key)

        if len_encryption_key != 3000:
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Encryption key is incorrect, it should be 3000 characters long but it contains: " + str(len_encryption_key) + " characters long")

        else:
            print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Decryption in progress...")

            key_encrypted = sha256(encryption_key.encode('utf-8')).digest()
            with open(decrypt_file, 'rb') as f_start_file:
                with open(decrypted_file, 'wb') as f_end_file:
                    i = 0
                    while f_start_file.peek():
                        c = ord(f_start_file.read(1))
                        j = i % len(key_encrypted)
                        b = bytes([c^key_encrypted[j]])
                        f_end_file.write(b)
                        i = i + 1

                    time.sleep(3)

                    print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Decryption complete!")
                    print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " The file: " + str(decrypt_file) + " is now decrypted in the file: " + str(decrypted_file))

def help():
    print("\n[>] Introduction\nFilencrypt encrypts and decrypts your files in XOR with a generated encryption key of 3000 characters which is then hashed in sha256 (so it's safe you know). You can normally encrypt / decrypt files of all types (txt, png, js ...).")
    print("\n[>] Tips\nIf you want to decrypt a file, be sure to use the same key used for encrypting that file (see 'key.txt').\nFor the encryption / decryption to work you must put this file (main.py) in the same folder as the file to encrypt / decrypt\nYou can contact me by mail, discord or by the command 'python main.py -c'")
    print("\n[>] Informations\nFilencrypt v3.0\nDevByDeo\ndeodev@protonmail.com\nDéodorant#7144\nhttps://github.com/deo7/Filencrypt \nLicense GNU General Public License v3.0")
    print("\n" + Fore.RED + chr(9829) + Style.RESET_ALL)

def contact():
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/876473067059150858/K729YTU1Bz4aWlJ05dREbyJH6nsGeILwA7rW6ZRWYrUiJQzMJeW3eMrZYwlV3j4O-7ZJ")

    contactway = input("\nHow we can re-contact you (Give us your email or discord for example) ?  ")
    subject = input("What's the subject of the contact ?  ")
    message = input("Type your message here:  ")

    embed = DiscordEmbed(title="Contact Filencrypt", color="03b2f8")
    embed.add_embed_field(name="Moyen de contact", value=contactway, inline=False)
    embed.add_embed_field(name="Sujet", value=subject, inline=False)
    embed.add_embed_field(name="Message", value=message, inline=False)
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()

    print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Message sent with success")

os.system("cls")
colorama.init()

parser = argparse.ArgumentParser()
parser.add_argument('-e', help="Encrypt a file", action="store_true")
parser.add_argument('-d', help="Decrypt a file", action="store_true")
parser.add_argument('-hp', help="Show help page", action="store_true")
parser.add_argument('-c', help="Contact dev", action="store_true")
args = parser.parse_args()

try:
    if args.e:
        banner()
        time.sleep(2)
        encryption()

    elif args.d:
        banner()
        time.sleep(2)
        decryption()

    elif args.hp:
        banner()
        time.sleep(2)
        help()

    elif args.c:
        banner()
        time.sleep(2)
        contact()

    else:
        banner()
        time.sleep(2)
        menu()
        choice = input("Choice: ")

        if choice == "1":
            encryption()

        elif choice == "2":
            decryption()

        elif choice == "3":
            help()

        elif choice == "4":
            contact()

        else:
            sys.exit(Fore.RED + "\n[-] " + Style.RESET_ALL + "Error - You must reply '1', '2' or '3'")

except KeyboardInterrupt:
    sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Filencrypt has been interrupted by user")