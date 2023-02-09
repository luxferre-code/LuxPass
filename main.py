from database import Database
from client import Client
from password import *
import cutie
from colorama import Fore, Style, init

# -- Constants -- #

DATABASE_NAME = "database.db"
LOGGER = False

if __name__ != "__main__": exit()

# -- Variables -- #

database = Database(DATABASE_NAME, logger=LOGGER)
client: Client = None
name: str = None
password: str = None

# -- Main code -- #

init()
name = input(f"{Fore.GREEN}Username: {Style.RESET_ALL}")
password = hash_password(cutie.secure_input(f"{Fore.GREEN}Password: {Style.RESET_ALL}"))

if(database.name_exists(name)):
    if(database.get_id(name, password) != None):
        client = Client(name, password, database)
        print(f"{Fore.GREEN}Logged in as {client}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Incorrect password{Style.RESET_ALL}")
        exit()
else:
    if(cutie.prompt_yes_or_no("Create new account?")):
        database.add_user(name, password)
        client = Client(name, password, database)
    else:
        input("Incorrect username or password. Press enter to exit...")
        exit()

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{Fore.BLUE}{Style.BRIGHT} ~= LuxPass =~ {Style.RESET_ALL}
    {Fore.GREEN}1. {Style.RESET_ALL}Ajout d'un mot de passe
    {Fore.GREEN}2. {Style.RESET_ALL}Afficher les mots de passe
    {Fore.GREEN}3. {Style.RESET_ALL}Supprimer un mot de passe
    {Fore.GREEN}4. {Style.RESET_ALL}Changer de mot de passe
    {Fore.GREEN}5. {Style.RESET_ALL}Quitter""")
    try:
        choice = input(f"{Fore.GREEN}Choix: {Style.RESET_ALL}")
        choice = int(choice)
    except ValueError:
        print(f"{Fore.RED}Choix invalide{Style.RESET_ALL}")
        continue

    if(choice == 1):
        name = input(f"{Fore.GREEN}Nom du mot de passe: {Style.RESET_ALL}")
        password = cutie.secure_input(f"{Fore.GREEN}Mot de passe: {Style.RESET_ALL}")
        password_confirm = cutie.secure_input(f"{Fore.GREEN}Confirmer le mot de passe: {Style.RESET_ALL}")
        if(password != password_confirm):
            print(f"{Fore.RED}Les mots de passe ne correspondent pas{Style.RESET_ALL}")
            continue
        password = encrypt_password(password, client.get_master_key())
        database.add_password(client.get_id(), name, password)
        print(f"{Fore.GREEN}Mot de passe ajouté{Style.RESET_ALL}")
    elif(choice == 2):
        passwords = database.get_passwords(client.get_id())
        if(len(passwords) == 0):
            print(f"{Fore.RED}Aucun mot de passe{Style.RESET_ALL}")
            continue
        for password in passwords:
            print(f"{Fore.GREEN}{password[0]}: {Style.RESET_ALL}{decrypt_password(password[1], client.get_master_key())}")

        input("Press enter to continue...")

    elif(choice == 3):
        passwords = database.get_passwords(client.get_id())
        if(len(passwords) == 0):
            print(f"{Fore.RED}Aucun mot de passe{Style.RESET_ALL}")
            continue
        for password in passwords:
            print(f"{Fore.GREEN}{password[0]}: {Style.RESET_ALL}{decrypt_password(password[1], client.get_master_key())}")
        name = input(f"{Fore.GREEN}Nom du mot de passe à supprimer: {Style.RESET_ALL}")
        if(database.remove_password(client.get_id(), name)):
            print(f"{Fore.GREEN}Mot de passe supprimé{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Mot de passe introuvable{Style.RESET_ALL}")

    elif(choice == 4):
        old_password = cutie.secure_input(f"{Fore.GREEN}Ancien mot de passe: {Style.RESET_ALL}")
        new_password = cutie.secure_input(f"{Fore.GREEN}Nouveau mot de passe: {Style.RESET_ALL}")
        new_password_confirm = cutie.secure_input(f"{Fore.GREEN}Confirmer le nouveau mot de passe: {Style.RESET_ALL}")
        if(new_password != new_password_confirm):
            print(f"{Fore.RED}Les mots de passe ne correspondent pas{Style.RESET_ALL}")
            continue
        if(database.change_password(client.get_id(), hash_password(old_password), hash_password(new_password))):
            print(f"{Fore.GREEN}Mot de passe changé{Style.RESET_ALL}")
            client = Client(client.get_username(), hash_password(new_password), database)
        else:
            print(f"{Fore.RED}Ancien mot de passe incorrect{Style.RESET_ALL}")

    elif(choice == 5):
        break

print(f"{Fore.GREEN}Au revoir{Style.RESET_ALL}")