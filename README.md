
# LuxPass

Ce programme est un gestionnaire de mots de passe sécurisé. Il utilise des technologies comme [SHA256](https://fr.wikipedia.org/wiki/SHA-2) et du [AES](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard). Il permet de sécurisé l'entièrete des mots de passe que vous voulez enregistrez.


## Installation

Il vous faut impérativement un environnement python 3.

**Pour les systèmes Linux/Windows**
```bash
git clone https://github.com/luxferre-code/LuxPass.git
cd LuxPass/
python3 -m pip install -r requirements.txt
python3 main.py
```
    
## Variables modifiables

Il est possible de modifier certains variables comme le nom de la base de donnée ou même si le mode __log__ est activé. Pour ce faire, modifier les lignes 9 -- 10 du fichier **main.py**

## Utilisation à l'IUT

Pour une utilisation sécurisé à l'IUT, après le premier démarrage du programme. Faite la commande suivant dans le repertoire du programme
```bash
chmod 700 * -R
```
Cette commande permet que aucune personne ne puissent accéder aux fichiers de votre LuxPass.


## Authors

- [@luxferre-code](https://www.github.com/luxferre-code)


## Utilisés par

Ce projet est utilisé que par moi :)


## License

[MIT](https://choosealicense.com/licenses/mit/)

