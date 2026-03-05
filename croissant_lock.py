#!/usr/bin/env python3
import urllib.request, json, ssl, tkinter as tk, os
from PIL import Image, ImageTk

# --- CONFIGURATION ---
API_URL = "https://nary14.pythonanywhere.com"
HOSTNAME = "pc_sedape"
IMG_NAME = "sedape.jpg" # Renomme ton image en sedape.jpg pour éviter les bugs d'accents
# ---------------------

class SedapeLock:
    def __init__(self, root):
        self.root = root
        
        # Setup plein écran total
        self.root.overrideredirect(True)
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none") # Cache la souris pour plus de réalisme
        
        # Touche de secours pour tes tests (Echap)
        self.root.bind("<Escape>", lambda e: self.quit_lock())

        # Chargement de l'image
        if not os.path.exists(IMG_NAME):
            self.root.configure(bg='red')
            tk.Label(root, text=f"ERREUR: {IMG_NAME} non trouvé", fg="white", bg="red", font=("Arial", 25)).pack(expand=True)
        else:
            try:
                img = Image.open(IMG_NAME).resize((root.winfo_screenwidth(), root.winfo_screenheight()))
                self.photo = ImageTk.PhotoImage(img)
                tk.Label(root, image=self.photo, borderwidth=0).pack()
            except Exception as e:
                print(f"Erreur image: {e}")

        print(f"[*] Surveillance du poste {HOSTNAME} lancée...")
        self.check_loop()

    def check_loop(self):
        try:
            # Bypass SSL pour éviter les erreurs de certificats sur Linux
            ctx = ssl._create_unverified_context()
            url = f"{API_URL}/status/{HOSTNAME}"
            
            with urllib.request.urlopen(url, context=ctx, timeout=3) as r:
                res = json.loads(r.read().decode())
                print(f"Serveur dit : {res['unlocked']}")
                
                if res['unlocked'] == True:
                    print("[!] Signal de déverrouillage reçu !")
                    
                    # AUTO-RESET : On demande au serveur de repasser en False immédiatement
                    try:
                        urllib.request.urlopen(f"{API_URL}/reset/{HOSTNAME}", context=ctx)
                        print("[*] Serveur réinitialisé pour la prochaine fois.")
                    except:
                        pass
                    
                    self.quit_lock()
                    return
        except Exception as e:
            print(f"Erreur réseau : {e}")
        
        # Vérifie toutes les 2 secondes
        self.root.after(2000, self.check_loop)

    def quit_lock(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SedapeLock(root)
    root.mainloop()
