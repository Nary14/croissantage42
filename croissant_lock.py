#!/usr/bin/env python3
import tkinter as tk
from PIL import Image, ImageTk
import os

# --- CONFIGURATION ---
IMAGE_FILE = "/home/traomeli/.config/autostart/img.jpg" # Remplace par le nom de ton image sedape
SECRET_KEY = "<Control-Alt-Key-x>" 
# ---------------------

class SedapeLock:
    def __init__(self, root):
        self.root = root
        
        # 1. Supprimer les bordures et forcer le plein écran
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
            print(f"Erreur : {e}")
            self.root.destroy()

        # 3. LE GRAB GLOBAL (C'est ça qui bloque la touche Windows)
        self.root.after(100, self.start_grab)

        # 4. Sécurités
        self.root.bind(SECRET_KEY, self.quit_lock)
        self.root.bind("<FocusOut>", lambda e: self.root.focus_force())

    def start_grab(self):
        # Capture tout le clavier et la souris
        self.root.grab_set_global()
        self.root.focus_force()

    def quit_lock(self, event):
        self.root.grab_release() # Très important de libérer avant de quitter
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SedapeLock(root)
    root.mainloop()
