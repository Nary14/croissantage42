#!/usr/bin/env python3
import urllib.request, json, ssl, tkinter as tk, os
from PIL import Image, ImageTk

# --- CONFIGURATION ---
API_URL = "https://nary14.pythonanywhere.com"
HOSTNAME = "pc_sedape"
IMG_NAME = "sedape.jpg" 

class SedapeLock:
    def __init__(self, root):
        self.root = root
        self.f8_count = 0
        
        self.root.overrideredirect(True)
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.attributes('-topmost', True)
        self.root.config(cursor="none")
        self.root.configure(bg='black')

        self.root.bind("<KeyRelease-F8>", self.secret_emergency_exit)
        
        if not os.path.exists(IMG_NAME):
            tk.Label(root, text="ERREUR IMAGE", fg="white", bg="red", font=("Arial", 25)).pack(expand=True)
        else:
            img = Image.open(IMG_NAME).resize((root.winfo_screenwidth(), root.winfo_screenheight()))
            self.photo = ImageTk.PhotoImage(img)
            tk.Label(root, image=self.photo, borderwidth=0).pack()

        # --- FIX: On attend que la fenêtre soit visible avant de grab ---
        self.root.after(500, self.start_grabbing)
        
        print(f"[*] Lock actif.")
        self.check_loop()

    def start_grabbing(self):
        try:
            self.root.focus_force()
            self.root.grab_set_global()
            print("[*] Clavier capturé avec succès.")
        except Exception as e:
            # Si ça rate, on réessaie un peu plus tard
            print(f"[*] Grab en attente... ({e})")
            self.root.after(500, self.start_grabbing)

    def secret_emergency_exit(self, event):
        self.f8_count += 1
        if self.f8_count >= 10:
            self.quit_lock()

    def check_loop(self):
        try:
            ctx = ssl._create_unverified_context()
            url = f"{API_URL}/status/{HOSTNAME}"
            with urllib.request.urlopen(url, context=ctx, timeout=3) as r:
                res = json.loads(r.read().decode())
                if res.get('unlocked') == True:
                    try:
                        urllib.request.urlopen(f"{API_URL}/reset/{HOSTNAME}", context=ctx)
                    except: pass
                    self.quit_lock()
                    return
        except: pass
        
        # On maintient le focus
        try:
            self.root.grab_set_global()
        except: pass
        
        self.root.after(2000, self.check_loop)

    def quit_lock(self):
        try: self.root.grab_release()
        except: pass
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SedapeLock(root)
    root.mainloop()
