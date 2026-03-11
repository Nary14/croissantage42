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

**Important:** Make sure that the image file (`sedape.jpg` by default) is located in the same directory as the `croissant_lock.py` script. If you use another path, modify the `IMAGE_PATH` variable in the script to use a relative path or a correct absolute path.

### Installation & Deployment

To deploy the tool quickly on a workstation, you can use the following one-liner:

```bash
git clone https://github.com/Nary14/croissantage42.git && cd croissantage42 && python3 croissant_lock.py
```

### Configuration

You should go at this link and tape BbobotaB_1242 to unlock your pc:

```link
https://nary14.pythonanywhere.com/
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

**Important**: This tool is designed for educational purposes only. It is not a replacement for proper system-level locking mechanisms (like `xlock` or your desktop environment's native lock feature).

For production security:
- Use your operating system's built-in lock screen
- Enable automatic screen lock after idle time
- Consider using encrypted workstations with proper authentication
 
## Contributing

This project is part of the 42 curriculum and is open for improvements and modifications.

## License

This project is created for educational purposes at 42.

---

**Stay secure and remember to lock your screen!**

