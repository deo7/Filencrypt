# Filencrypt v4.0 💖
Filencrypt is a cryptography project started in 2021 that encrypts and decrypts your files of all extensions (txt, js, png...) in AES-256 CBC Mode. Filencrypt works with a password chosen by the user and with an initialization vector (IV) generated by the program.

# Use 💻
## Installation
```bash
git clone https://github.com/deo7/Filencrypt.git
cd Filencrypt
pip install -r requirements.txt
```

## Run
Windows :
```
python filencrypt.py [-h] [-e] [-d] [-i] [-c]
```

Linux :
```
python3 filencrypt.py [-h] [-e] [-d] [-i] [-c]
```

# Demonstartion 📸
![demo1](demos/demo1.png)

As you can see above, I encrypt a 'test.txt' file with the password 'Filencrypt'. Thus, the original content of this file become encrypted and unreadable. <br />
The program creates a file 'AES_IV.txt' containing the initialization vector (IV) used for the AES encryption of THIS file (and only this file, a file encryption -> a new IV generated). The IV is a 128 byte block uses by AES-256 CBC Mode for encryption.<br />
AES_IV.txt file :

![demo2](demos/demo2.png)

Finally, I decrypt my file with the password AND initialization vector (see below).<br />
- WARNING : If you decrypt your file with an incorrect password / IV, you will get errors and incorrect decryption.

![demo3](demos/demo3.png)

To conclude, here is a table that resume the encryption and the decryption of 'test.txt' :

| Original file content | Encrypted file content (with my password and my IV) | Decrypted file content |
| :---                  |     :---:                                           |                   ---: |
| Hello world !         | ßCï‰€å2µÄ£ËÅPð                                    | Hello world !          |

# Other 📚
<p align="center">
  <img src="https://img.shields.io/github/stars/deo7/filencrypt?style=for-the-badge&color=yellow">
  <img src="https://img.shields.io/badge/Version-4-green?style=for-the-badge">
  <img src="https://img.shields.io/github/license/deo7/filencrypt?style=for-the-badge&color=red"><br />
  <img src="https://img.shields.io/badge/Author-Déodorant%237144-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Lines of codes-277-brown?style=for-the-badge">
</p>
