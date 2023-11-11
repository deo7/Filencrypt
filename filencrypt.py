
try:
    from colorama import Fore, Style
    from colorama.initialise import reset_all
    from hashlib import sha256
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from Crypto.Cipher import AES
    from Crypto.Util import Padding
    from urllib.request import Request
    import pyfiglet
    import hashlib
    import argparse
    import urllib.request
    import random
    import timeit
    import string
    import time
    import sys
    import os
    import colorama
except:
    sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing requirements. Run 'pip install -r requirements.txt' and re-try.")

def banner():
    try:
        pfbanner = pyfiglet.figlet_format("Filencrypt", font="graffiti")
        print(pfbanner)
        print("                 Made with", Fore.RED, chr(9829), Style.RESET_ALL, "by Déodorant#7144")
        print("               https://github.com/deo7/Filencrypt")
    except pyfiglet.FontNotFound:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Banner error. Run 'sudo pip3 install --upgrade pyfiglet' and re-try.")

def menu():
    print("\n\nMenu")
    print("[1] Encrypt")
    print("[2] Decrypt")
    print("[3] Informations")
    print("[4] Contact dev")

def encryption():
    def filencrypt(pswd, iv, file):
        key = hashlib.sha256(pswd.encode()).digest()

        with open("AES_IV.txt", "w") as ivf:
            ivf.write(f"Encryption of : {file}\n\n-----BEGIN AES INITIALIZATION VECTOR BLOCK-----\n{iv}\n-----END AES INITIALIZATION VECTOR BLOCK-----".replace("b'", "").replace("'", ""))

        with open(file, "rb") as f:
            data = f.read()

        stime = timeit.default_timer()
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        paddeddata = Padding.pad(data, 16)
        encrypteddata = cipher.encrypt(paddeddata)
        
        with open(file, "wb") as ef:
            ef.write(encrypteddata)

        time = timeit.default_timer() - stime

        print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Encryption of the file " + Fore.GREEN + str(file) + Style.RESET_ALL + " complete in " + Fore.GREEN + str(round(time, 3)) + Style.RESET_ALL + " seconds!\n")
        print("Don't forget the password you used for the encryption of this file!\nAlso a " + Fore.GREEN + "AES_IV.txt " + Style.RESET_ALL + "file has been created, it contains the initialization vector (IV) of the encryption. " + Fore.RED + "\nYou have to keep this file " + Style.RESET_ALL + "because you will need this IV for decrypt your file.")

    file = input(Fore.YELLOW + "\nFile to encrypt : " + Style.RESET_ALL)

    if "." in file:
        pass
    else:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing extension")

    try:
        with open(file, "rb"):
            pass
    except IOError:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + f" Error - File not found. Make sure your file is in this path : {os.path.realpath(__file__).replace('filencrypt.py', '')}")

    if os.path.getsize(file) > 62914560:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File too large. Max size is 60Mo to avoid crashes or errors.")
    else:
        pass

    pswd = input(Fore.YELLOW + "Choose a strong password : " + Style.RESET_ALL)

    def geniv(length):
        str = string.ascii_uppercase + string.digits #+ string.punctuation
        return "".join(random.choice(str) for i in range(length))

    iv = geniv(16)
                
    filencrypt(pswd, iv.encode(), file)

def decryption():
    def filedecrypt(pswd, iv, file):
        key = hashlib.sha256(pswd.encode()).digest()

        with open(file, "rb") as f:
            data = f.read()

        stime = timeit.default_timer()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypteddata = cipher.decrypt(data)
        unpaddeddata = Padding.unpad(decrypteddata, 16)

        with open(file, "wb") as ef:
            ef.write(unpaddeddata)
    
        time = timeit.default_timer() - stime

        print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Decryption of the file " + Fore.GREEN + str(file) + Style.RESET_ALL + " complete in " + Fore.GREEN + str(round(time, 3)) + Style.RESET_ALL)
    
    file = input(Fore.YELLOW + "\nFile to decrypt : " + Style.RESET_ALL)

    if "." in file:
        pass
    else:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing extension")

    try:
        with open(file, "rb"):
            pass
    except IOError:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File not found. Make sure your file is in this path : {os.path.realpath(__file__).replace('filencrypt.py', '')}")

    pswd = input(Fore.YELLOW + f"Password used to encrypt {file} : " + Style.RESET_ALL)
    iv = input(Fore.YELLOW + f"IV used to encrypt {file} : " + Style.RESET_ALL)

    if len(iv) != 16:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + f" Error - Incorrect length of initialization vector : {len(iv)} chars instead of 16.")

    filedecrypt(pswd, iv.encode(), file)

def about():
    print(Fore.YELLOW + f"\n[>] Running file : {os.path.realpath(__file__)}" + Style.RESET_ALL)
    print("\n[>] Presentation\nFilencrypt (currently in version 4.0) is a cryptography project started in 2021 that encrypts and decrypts your files of all types (js, txt, png...) in AES-256. Filencrypt works with a strong password chosen by the user and with a 16 byte initialization vector (IV) generated by the program, you must keep this IV secret and you will need it to decrypt your file. Note that a new IV is created for each encrypted file.")
    print("\n[>] Security\nIs Filencrypt a secure project?\nFilencrypt uses AES-256-bit encryption with Cipher Block Chaining (CBC) mode. Although CBC Mode is less secure than XTS or GCM Modes, it is generally suitable for encrypting more or less sensitive files.\nSecurity also depends on the password you use, you should use a strong password with uppercase, lowercase, symbols and numbers.")
    print("\nIf you have any other questions or suggestions, contact me by discord (Déodorant#7144), mail (deodorantdev@protonmail.com) or by running 'python filencrypt.py -c'!")

def contact():
    global os

    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl")

    req = Request(
        url="https://discord.com/api/webhooks/908820502343188501/uljt9W1cqtff0PH5ZzAjvZKxTDfPCioFwYwM8WAgRXBPYbLFRCTGdBz5CvAD4_8_Hzcl",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            txt = response.read()
    except:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Contact system error. Try to contact me by discord (Déodorant#7144) or by mail (deodorantdev@protonmail.com).")

    contactway = input(Fore.YELLOW + "\nEmail or discord to be contacted : " + Style.RESET_ALL)
    subject = input(Fore.YELLOW + "Subject : " + Style.RESET_ALL)
    message = input(Fore.YELLOW + "Message : " + Style.RESET_ALL)

    if contactway == "" or subject == "" or message == "":
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Empty inputs")

    img = input(Fore.YELLOW + "Add an image ('y' or 'n') : " + Style.RESET_ALL)
    if img == "y":
        filepath = input(Fore.YELLOW + "Path of image : " + Style.RESET_ALL)

        try:
            with open(filepath, 'rb'):
                pass
        except IOError:
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Image not found")

        if os.path.getsize(filepath) > 8388608:
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File too large. Max size is 8Mo.")
        else:
            pass
        
        with open(filepath, "rb") as f:
            webhook.add_file(file=f.read(), filename="file.png")
    else:
        pass

    embed = DiscordEmbed(title="Contact Filencrypt", color="03b2f8")
    embed.add_embed_field(name="Moyen de contact", value=contactway, inline=False)
    embed.add_embed_field(name="Sujet", value=subject, inline=False)
    embed.add_embed_field(name="Message", value=message, inline=False)

    proxy = {
        "http": "14.97.216.232:80"
    }
    webhook.set_proxies(proxy)
    webhook.add_embed(embed)
    response = webhook.execute()

    print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Message sent with success")

if sys.platform.startswith("linux"):
    os.system("clear")
elif sys.platform.startswith("win32"):
    os.system("cls")
else:
    pass

colorama.init()

parser = argparse.ArgumentParser()
parser.add_argument('-e', help="Encrypt a file", action="store_true")
parser.add_argument('-d', help="Decrypt a file", action="store_true")
parser.add_argument('-i', help="Informations", action="store_true")
parser.add_argument('-c', help="Contact dev", action="store_true")
args = parser.parse_args()

try:
    if args.e:
        banner()
        encryption()

    elif args.d:
        banner()
        decryption()

    elif args.i:
        banner()
        about()

    elif args.c:
        banner()
        contact()
        
    else:
        banner()
        menu()
        choice = input("Choice: ")

        if choice == "1":
            encryption()

        elif choice == "2":
            decryption()

        elif choice == "3":
            about()

        elif choice == "4":
            contact()

        else:
            sys.exit(Fore.RED + "\n[-] " + Style.RESET_ALL + "Error - You must reply '1', '2', '3' or '4'")

except KeyboardInterrupt:
    sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Filencrypt has been interrupted by user")