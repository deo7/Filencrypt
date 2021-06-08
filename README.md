# CryptMyFile 💖
CryptMyFile chiffre et déchiffre vos fichiers de tous types (png, js, txt...) en XOR avec une clé de chiffrement générée de 3000 caractères (par la suite hashée en sha-256)

# Installation 🛠
```bash
git clone https://github.com/deo7/CryptMyFile.git
cd CryptMyFile
pip install -r requirements.txt
```

# Utilisation 💻
## Run
```python
python main.py
```
## Conseils
* Veillez bien à mettre le fichier principal 'main.py' dans le même dossier que le fichier à chiffrer

* N'oubliez pas l'extension lorsque le programme vous demande le nom du fichier

* Si vous voulez déchiffrer un fichier, veillez à utiliser la même clé utilisée lors du chiffrement de celui-ci (celle-ci est dans 'key.txt')

Plus d'infos dans la partie aide du programme

# Demonstartion 📸
![demo1](demos/1.png)

![demo2](demos/2.png)

Comme vous pouvez le voir ci-dessus j'ai choisis de chiffrer un fichier 'fichier.js' dans un fichier 'chiffrer.txt', en gros le contenu de 'fichier.js' va être chiffré puis écrit dans 'chiffrer.txt'. J'aurais très bien pu changer l'extension et choisir de chiffré 'fichier.js' vers 'chiffrer.rb'.

![demo3](demos/3.png)

J'ai ensuite choisis de déchiffrer mon fichier 'chiffrer.txt' vers un fichier C#, 'dechiffrer.cs'. Pour ce faire, j'ai relancer le programme avec `python main.py` puis j'ai sélectionné la langue (en l'occurence `1` pour le français) puis j'ai sélectionné `2` pour déchiffrer mon fichier.

Attention: pour que le déchiffrement soit correcte j'ai utilisé la même clé que pour chiffrer le fichier. Cette clé de chiffrement fait 3000 caractères et est automatiquement générée par le programme lors du chiffrement de votre fichier, elle est ensuite écrite dans un fichier appelé 'key.txt' dans le même dossier que celui où est 'main.py'. Si la clé de chiffrement est incorrecte, le déchiffrement de votre fichier sera incorrect.

![demo4](demos/4.png)

Pour conclure, voici un `cat` de tous les fichier, le fichier de départ 'fichier.js', puis le fichier chiffré 'chiffrer.txt', et enfin le fichier déchiffré 'dechiffrer.cs'.

# Légal 🎓
Conformément à la license GNU General Public License v3.0, et comme explicitement indiqué dans celle-ci, vous avez des autorisations et des obligations vis-à-vis de ce projet que vous pouvez retrouver [juste ici](https://choosealicense.com/licenses/gpl-3.0/)

# Contact 📩
Vous pouvez me contacter
* Via Discord: Déodorant#7144
* Par mail: deodev@protonmail.com
