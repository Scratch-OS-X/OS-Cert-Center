# OS Certificates Center

## Introduction :
Tous les codes utilisés par **_Scratch OS certificate center_** sont réunis dans ce dépot.

## Generateur-de-codes(.py)
Le fichier [`Generateur-de-codes.py`](/Generateur-de-codes.py) sert à **générer des codes** (ex : `ABC-123-def`)

```Python
import random
import string

def generer_code():
    ABC = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    _123 = ''.join(random.choice(string.digits) for _ in range(3))
    def = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    return f"{ABC}-{_123}-{def}"

print(generer_code())
```

## Cert-Finder(.py) :
Le fichier [`Cert-Finder.py`](/Cert-Finder.py) sert à **rechercher** des certificats et à obtenir des informations dessus (comme un mini moteur de recherche) à partir du code d'un certificat (ex : `ABC-123-def`)

```Python
import requests
import os
import time
import re



Certificat = input("Rechercher un certificat (ex : `ABC-123-def`) >>> ")

if re.fullmatch(r"^[A-Z]{3}-\d{3}-[a-z]{3}$", Certificat):
  if Certificat == "LHF-557-vvm":
    print(f"Certificat n° \033[1m{Certificat}\033[0m \033[32m ✔ Ok\033[0m")
    print("Créateur : \033[1m Scratch_2_0_2_4\033[0m \033[34m vérifié \033[0m")
    print("Nom de l'OS : \033[1m Scratch.OS X\033[m")
  elif Certificat == "ABC-123-def":
     print(f"Certificat n° \033[1m{Certificat}\033[0m \033[33m certificat exemple \033[0m")
  else :
     print(f"\033[31m ✖ Le certificat \033[1m{Certificat}\033[m \033[31m n'existe pas.\033[0m")
elif Certificat == "ADMIN" :
  print("ADMIN Mode")
  ADMIN = input("Administration >>> ")
elif Certificat == "help" :
  print("Commandes : ")
  print("• Recherche de certificats")
else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m \033[0m")
```

## ADMIN(.py)
Le fichier [`ADMIN.py`](/ADMIN.py) sert à a **modifier** des certificats à partir de leur code (ex : `ABC-123-def`) et d'un mot de passe.

```Python
import re
import os

pattern = r"^[A-Z]{3}-\d{3}-[a-z]{3}$"
admin = input("Certificat >>> ")

MDP_LHF = os.getenv('MDP_LHF_VVM')

if re.fullmatch(pattern, admin):
    if admin == "LHF-557-vvm":
        mdp = input("Mot de Passe ? >>> ")
        if MDP_LHF == mdp:
            print("\033[32m ✔ Ok\033[0m")
            print("Mode ADMIN à venir")
        else:
            print("\033[31m ✖ Mot de Passe invalide \033[0m")
    else:
        print("\033[31m ✖ Non-trouvé. \033[0m")
else:
    print("\033[31m ✖ Format invalide. Format correct : \033[1m ABC-123-def \033[0m \033[0m")
```
