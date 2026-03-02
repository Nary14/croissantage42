*This project has been created as part of the 42 curriculum by traomeli.*

# Sedape (Lockscreen Security Tool)

## Description

**Sedape** is a Python-based security education tool developed at 42.
The goal of this project is to simulate a system "lock" by displaying a full-screen warning image, commonly known in the 42 community as a "croissantage" (or here, a "sedape").
It serves as a humorous but effective reminder for students to lock their sessions when leaving their workstations.

The script captures keyboard and mouse events to prevent easy bypass, requiring a specific secret key combination to release the screen.

## Instructions

### Prerequisites

Since the script uses the Python Imaging Library (PIL), you need to install `Pillow` locally (no sudo required):

```bash
pip3 install --user Pillow
```

⚠️ **Important** : Assurez-vous que le fichier image (`img.jpg` par défaut) se trouve dans le même répertoire que le script `croissant_lock.py`. Si vous utilisez un autre chemin, modifiez la variable `IMAGE_PATH` dans le script pour utiliser un **chemin relatif** ou un chemin absolu correct.

### Installation & Deployment

To deploy the tool quickly on a workstation, you can use the following one-liner:

```bash
git clone https://github.com/Nary14/croissantage42.git && cd croissantage42 && python3 croissant_lock.py
```

### Configuration

You can customize the unlock combination in the script:

```python
# Exemple: Ctrl + Alt + X
SECRET_KEY = "<Control-Alt-Key-x>"
```

## Usage

Once installed, simply run the script:

```bash
python3 croissant_lock.py
```

The lockscreen will immediately activate:
- A full-screen warning image will be displayed
- All keyboard and mouse inputs will be captured
- The system will remain locked until the correct key combination is entered
- Press the configured `SECRET_KEY` to unlock and return to your session

## Features

- **Full-screen Display**: Blocks the entire screen with a warning image
- **Input Interception**: Captures and prevents keyboard and mouse events
- **Customizable Unlock Key**: Easy configuration of the secret key combination
- **Lightweight**: Minimal resource usage
- **Educational Purpose**: Teaches security awareness and session management

## Security Notes

⚠️ **Important**: This tool is designed for educational purposes only. It is not a replacement for proper system-level locking mechanisms (like `xlock` or your desktop environment's native lock feature).

For production security:
- Use your operating system's built-in lock screen
- Enable automatic screen lock after idle time
- Consider using encrypted workstations with proper authentication

## Troubleshooting

### Erreur : `[Errno 2] No such file or directory: '..../img.jpg'`

**Cause** : Le script ne trouve pas le fichier image.

**Solution** :
1. Vérifiez que le fichier `img.jpg` existe bien dans le répertoire du projet
2. Si vous utilisez une autre image, modifiez la variable `IMAGE_PATH` dans le script :
   ```python
   IMAGE_PATH = "img.jpg"  # Chemin relatif (recommandé)
   # OU
   IMAGE_PATH = os.path.join(os.path.dirname(__file__), "img.jpg")  # Chemin absolu dynamique
   ```
3. Assurez-vous de lancer le script depuis le répertoire du projet :
   ```bash
   cd croissantage42
   python3 croissant_lock.py
   ```

### Erreur : `TclError: can't invoke "bind" command: application has been destroyed`

**Cause** : L'application Tkinter se ferme à cause d'une erreur (souvent liée à l'image manquante).

**Solution** :
1. Résolvez d'abord l'erreur du fichier image (voir ci-dessus)
2. Vérifiez que `python3-tk` est bien installé (voir section Prerequisites)
3. Testez avec : `python3 -m tkinter` (une fenêtre devrait s'ouvrir)

### Le lockscreen ne se déverrouille pas
- Assurez-vous d'utiliser la combinaison exacte définie dans `SECRET_KEY`
- Vérifiez votre disposition de clavier (les codes peuvent varier)
- Vérifiez que le script est toujours en cours d'exécution

### Problèmes d'affichage
- Vérifiez que Pillow est bien installé : `pip3 list | grep Pillow`
- Vérifiez que votre écran supporte le mode plein écran
- Si l'image ne s'affiche pas correctement, vérifiez son format (JPG ou PNG recommandés)

## Contributing

This project is part of the 42 curriculum and is open for improvements and modifications.

## License

This project is created for educational purposes at 42.

---

**Stay secure and remember to lock your screen!** 🔐

