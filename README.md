![ClipMinder Banner](ClipMinder.png)

_"Transform your workflow with the power of effortless text management, and let every keystroke be a symphony of productivity."_

**ClipMinder** is a powerful and versatile clipboard manager designed to enhance your productivity by providing easy access to predefined text snippets. Developed by Bohdan Misonh, this tool is perfect for users who frequently need to copy and paste various text blocks, allowing for quick and efficient text management.

## Features

- **Clipboard Expansion**: Seamlessly manage multiple text snippets with predefined blocks. Access up to 8 different text blocks with customizable hotkeys.
- **Copy and Paste Automation**: Not only can you copy text snippets to your clipboard, but you can also automate pasting for faster workflows.
- **Customizable Hotkeys**: Easily redefine hotkeys to fit your workflow preferences. Whether you need to use single keys or combinations, ClipMinder adapts to your needs.
- **Pause and Resume Functionality**: Pause the program with a simple key combination and resume whenever needed, ensuring uninterrupted productivity.
- **File Opening**: Quick access to your `predefined_clips.txt` file for easy editing and updates.

## Installation

To use ClipMinder, you need to have Python installed on your system. You also need to install the required Python libraries. Follow these steps:

   ```bash
   git clone https://github.com/raikoho/ClipMinder.git
   cd ClipMinder
   pip install -r requirements.txt
   python clipminder.py
   ```
## Usage
When you run ClipMinder, you'll be greeted with an introduction screen and prompted to choose an option:

1) Copy Only: Select this option to enable text copying with predefined hotkeys.
2) Copy and Paste: Choose this to enable automatic pasting of copied text.
3) Redefine Keys: Customize the hotkeys for various actions including copying, clearing the clipboard, and opening the file.
Your file - **predefined_clips.txt** aims to establish your own text for future copying. Set the text directly in the block (between the end and the beginning). It looks something like this:

>---START---

>First copy = Alt+1

>---END---


>---START---

>Друге Копіювання (2)

>---END---


>---START---

>3Copy = Number 3 = Alt+3

>---END---

#### Example Hotkeys
- Alt+1 to Alt+8: Copy corresponding text blocks.
- Alt+9: Clear the clipboard.
- Alt+0: Open the predefined_clips.txt file.
- Alt+Space: Pause/Start using program/smart buffer.

## Redefining Keys
To redefine keys, select the "Redefine Keys" option and follow the prompts. You can set new key combinations for each action or restore the default settings. Key formats include single keys, combinations like alt+1, or multiple keys such as ctrl+shift+z. 
You can also choose an ordinary letter or number - in this case, the program will leave behind a clean copy without this symbol.

## Example Use Case
Imagine you often need to copy different sections of a report or frequently used email responses. Instead of manually copying and pasting each time, you can set up ClipMinder with these snippets and access them instantly with the press of a hotkey. For example, pressing Alt+1 might copy your standard greeting, and Alt+2 could copy your closing statement, saving you valuable time and effort. And you can make the choice even bigger.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries or feedback, you can reach out to the project maintainer:
Bohdan Misonh - https://www.linkedin.com/in/bohdan-misyonh/

## Thank you for using ClipMinder, and happy clipping!
