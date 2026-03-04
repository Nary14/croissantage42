#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
import os

# --- CONFIGURATION ---
IMAGE_FILE = "vous avez été sédapé.png"
# Ton nouveau mot de passe (secret)
SECRET_PASSWORD = "traomeli@student.42antananarivo.mg"
# ---------------------

class SedapeLock:
    def __init__(self, root):
        self.root = root
        self.typed_buffer = "" # Stocke les dernières touches tapées
        
        # 1. Configuration plein écran et priorité maximale
        self.root.overrideredirect(True) 
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none")
        self.root.configure(background='black')

        # 2. Chargement de l'image
        try:
            img = Image.open(IMAGE_FILE)
            img = img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.label = tk.Label(root, image=self.photo, borderwidth=0)
            self.label.pack(expand=True, fill="both")
        except Exception as e:
            print(f"Erreur chargement image : {e}")
            self.root.destroy()

        # 3. LE GRAB GLOBAL (Bloque tout le système)
        self.root.after(100, self.start_grab)

        # 4. Écoute globale du clavier (Binding pour le mot de passe)
        self.root.bind_all("<Key>", self.check_password)
        
        # Empêche de perdre le focus (si l'utilisateur essaie de cliquer ailleurs)
        self.root.bind("<FocusOut>", lambda e: self.root.focus_force())

    def start_grab(self):
        # Capture tout le clavier et la souris au niveau du système
        self.root.grab_set_global()
        self.root.focus_force()

    def check_password(self, event):
        # On ignore les touches de fonction (Shift, Ctrl, etc.) qui n'ont pas de caractère
        if event.char:
            self.typed_buffer += event.char
            
            # On ne garde en mémoire que les derniers caractères (longueur du mot de passe)
            self.typed_buffer = self.typed_buffer[-len(SECRET_PASSWORD):]
            
            # Vérification du mot de passe
            if self.typed_buffer == SECRET_PASSWORD:
                self.quit_lock()

    def quit_lock(self):
        # Libère les contrôles et ferme la fenêtre
        self.root.grab_release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SedapeLock(root)
    root.mainloop()
