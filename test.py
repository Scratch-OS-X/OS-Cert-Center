import acceptlicense as l
import sqlite3
import re

conn = sqlite3.connect('DB.SQLite')
cursor = conn.cursor()

l.accept_license()

with open('script.sql', 'r') as f:
    cursor.executescript(f.read())
conn.commit()

while True:
    Certificat = input("Rechercher un certificat (ex : ABC-123-def) >>> ")

    if re.fullmatch(r"^[A-Z]{3}-\d{3}-[a-z]{3}$", Certificat):
    cursor.execute(
        'SELECT "créateur", "OS_Name" FROM "OS-Cert-Center" WHERE "id" = ?',
        (Certificat,)
    )
    result = cursor.fetchone()

        if result:
            createur, os_name = result
            print(f"Certificat n° \033[1m{Certificat}\033[0m \033[32m ✔ Ok\033[0m")
            print(f"Créateur : \033[1m {createur}\033[0m")
            print(f"Nom de l'OS : \033[1m {os_name}\033[m")
        else:
            print(f"\033[31m ✖ Le certificat \033[1m{Certificat}\033[0m] \033[31m n'existe pas.\033[0m")
    else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m")

    conn.close()