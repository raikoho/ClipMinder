import keyboard
import pyperclip
import time
import os
import sys
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Path to the file with text snippets
CLIPS_FILE = 'predefined_clips.txt'


# Reading text snippets from the file
def read_clips(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    clips = content.split('---START---')[1:]
    clips = [clip.split('---END---')[0].strip() for clip in clips]
    return clips


# Copying text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)


# Pasting text
def paste_from_clipboard():
    keyboard.press_and_release('ctrl+v')


def user_choice():
    print(Fore.CYAN + "Choose an option:")
    print(Fore.CYAN + "1) Copy to buffer only")
    print(Fore.CYAN + "2) Copy to buffer and immediately paste")
    print(Fore.CYAN + "3) Redefine keys")
    choice = input(Fore.YELLOW + "Your choice (1/2/3): ")
    return choice


# Redefining keys
def redefine_keys():
    print(Fore.CYAN + "Redefine keys:")
    print(Fore.CYAN + "1) Enter new keys")
    print(Fore.CYAN + "2) Restore default keys")
    option = input(Fore.YELLOW + "Your choice (1/2): ")

    key_mapping = {
        '1': 'alt+1',
        '2': 'alt+2',
        '3': 'alt+3',
        '4': 'alt+4',
        '5': 'alt+5',
        '6': 'alt+6',
        '7': 'alt+7',
        '8': 'alt+8',
        '9': 'alt+9',
        '0': 'alt+0'
    }

    if option == '2':
        print(Fore.GREEN + "Default key combinations restored.")
    else:
        print(Fore.CYAN + "For each copy action, you can specify the desired key combination (e.g., 'alt+1').")
        print(Fore.CYAN + "Correct format for special keys: alt, shift, tab, 0-9 (numbers), a-z;")
        print(Fore.CYAN + "You can enter a single key or a combination in the format: key or key+key or key+key+key.")

        for key in key_mapping:
            new_key = input(Fore.YELLOW + f"Enter new combination for copy {key} (current: {key_mapping[key]}): ")
            if new_key:
                key_mapping[key] = new_key

    print(Fore.GREEN + "\nKey redefinition completed.")
    return key_mapping


def open_file(file_path):
    try:
        if sys.platform == "win32":
            os.startfile(file_path)
        elif sys.platform == "darwin":
            os.system(f"open {file_path}")
        else:
            os.system(f"xdg-open {file_path}")
    except Exception as e:
        print(Fore.RED + f"Failed to open file: {e}")


def show_intro():
    print(Fore.MAGENTA + """
     ____ _         __  __ _           _           
    / ___| (_) ___ |  \/  (_)_ __   __| | ___ _ __ 
   | |  _| | |/ _  \ |\/| | | '_ \ / _` |/ _ \ '__|
   | |_| | | || |_ | |  | | | | | | (_| |  __/ |   
    \____|_|\_| |__/_|  |_|_|_| |_|\__,_|\___|_|   
              |_|
    """)
    print(Fore.GREEN + "ClipMinder - a tool to expand and facilitate the copy buffer")
    print(Fore.YELLOW + "by Bohdan Misonh, version 0.9\n")


# Main function
def main():
    show_intro()
    clips = read_clips(CLIPS_FILE)
    key_mapping = {
        '1': 'alt+1',
        '2': 'alt+2',
        '3': 'alt+3',
        '4': 'alt+4',
        '5': 'alt+5',
        '6': 'alt+6',
        '7': 'alt+7',
        '8': 'alt+8',
        '9': 'alt+9',
        '0': 'alt+0'
    }
    mode = user_choice()

    if mode == '3':
        key_mapping = redefine_keys()
        mode = user_choice()

    if mode == '1':
        print(Fore.CYAN + f"Press {key_mapping['1']} to {key_mapping['8']} to copy text.")
        print(Fore.CYAN + f"Press {key_mapping['9']} to clear the clipboard.")
        print(Fore.CYAN + f"Press {key_mapping['0']} to open the file.")
    elif mode == '2':
        print(Fore.CYAN + f"Press {key_mapping['1']} to {key_mapping['8']} to copy and automatically paste text.")
        print(Fore.CYAN + f"Press {key_mapping['9']} to clear the clipboard.")
        print(Fore.CYAN + f"Press {key_mapping['0']} to open the file.")

    try:
        while True:
            for i in range(8):
                if keyboard.is_pressed(key_mapping.get(str(i + 1), f'alt+{i + 1}')):
                    text = clips[i]
                    copy_to_clipboard(text)
                    print(Fore.GREEN + f"Copied block {i + 1}: {text}")
                    if mode == '2':
                        time.sleep(0.5)#FOR DELAY AFTER COPY AND BEFORE PASTE
                        paste_from_clipboard()
                        print(Fore.GREEN + "Text pasted.")
                    if '+' not in key_mapping.get(str(i + 1), f'alt+{i + 1}'):  # Remove character if it's a single key
                        keyboard.press_and_release('backspace')
                    time.sleep(0.5)
            if keyboard.is_pressed(key_mapping.get('9', 'alt+9')):
                pyperclip.copy('')
                print(Fore.GREEN + "Clipboard cleared.")
                time.sleep(0.5)
            if keyboard.is_pressed(key_mapping.get('0', 'alt+0')):
                open_file(CLIPS_FILE)
                time.sleep(0.5)

            # Pause the program
            if keyboard.is_pressed('alt+space'):
                print(Fore.YELLOW + "Program paused. Press Alt+Space to resume.")

                while keyboard.is_pressed('alt+space'):
                    time.sleep(0.1)

                while not keyboard.is_pressed('alt+space'):
                    time.sleep(0.1)

                while keyboard.is_pressed('alt+space'):
                    time.sleep(0.1)
                print(Fore.YELLOW + "Program resumed.")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram terminated.")
        sys.exit(0)


if __name__ == "__main__":
    main()