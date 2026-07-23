import re

def run():
    # Vérification si les modules requis sont bien installés
    try:
        import barcode
        from barcode.writer import ImageWriter
    except ImportError:
        print("❌ python-barcode ou pillow non installé!")
        print('Installe avec: pip3 install "python-barcode[images]" (macOS/Linux) ou pip install "python-barcode[images]" (Windows).')
        return

    couleurs = ["black", "white", "red", "green", "blue", "yellow", "cyan", "magenta"]

    while True:
        print("Codes barres (Code 128) [v. 1.1]")
        print("Entre 'exit' à tout moment pour quitter.\n")
        
        texte = input("Code du certificat (ex : ABC-123-def) >>> ").strip()

        if not texte:
            print("❌ Entrée vide!\n")
            continue

        if texte.lower() == "exit":
            print("Au revoir !")
            break

        print(f"\nCouleurs disponibles: {', '.join(couleurs)}")

        # Validation couleur des barres
        while True:
            foreground = input("Couleur des barres [défaut: black] >>> ").strip() or "black"
            if foreground in couleurs or foreground.startswith("#"):
                break
            print(f"❌ Couleur invalide! Choisis parmi: {', '.join(couleurs)}")

        # Validation couleur du fond
        while True:
            background = input("Couleur du fond [défaut: white] >>> ").strip() or "white"
            if background in couleurs or background.startswith("#"):
                break
            print(f"❌ Couleur invalide! Choisis parmi: {', '.join(couleurs)}")

        # Options d'écriture d'image avec personnalisation des couleurs
        writer_options = {
            'module_color': foreground,
            'background': background
        }

        # Création du code-barres Code 128
        Code128 = barcode.get_barcode_class('code128')
        mon_code = Code128(texte, writer=ImageWriter())

        # Nettoyage du nom de fichier
        safe_name = re.sub(r'[^\w\-.]', '_', texte)
        if len(safe_name) > 30:
            safe_name = safe_name[:30]

        filename = f"{safe_name}"

        # Sauvegarde (ImageWriter ajoute automatiquement le .png à la fin)
        fichier_final = mon_code.save(filename, options=writer_options)
        print(f"✅ Code-barres sauvegardé en : {fichier_final}\n")


if __name__ == "__main__":
    run()
