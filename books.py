import os
import subprocess
from blessed import Terminal

def list_supported_files(directory):
    return [f for f in os.listdir(directory) if f.endswith(('.epub', '.pdf'))]

def is_japanese(text):
    for char in text:
        if ord(char) >= 0x4E00 and ord(char) <= 0x9FFF:
            return True
    return False

def open_file(file):
    if file.endswith('.epub') and is_japanese(file):
        subprocess.run(['zathura', file])
    elif file.endswith('.epub'):
        subprocess.run(['epy', file])
    elif file.endswith('.pdf') or is_japanese(file):
        subprocess.run(['zathura', file])

def main():
    term = Terminal()
    directory = 'Documents/Books/'  # Adjust the directory as per your setup

    files = list_supported_files(directory)

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        key = ''
        index = 0

        while key.lower() != 'q':
            output = term.clear() + term.center(term.bold('Ebook Library')) + '\n\n'
            
            # Calculate the number of rows that can fit in the terminal
            max_rows = term.height - 4
            
            # Calculate the start and end indexes for displaying files
            start_index = max(0, index - max_rows // 2)
            end_index = min(len(files), start_index + max_rows)

            for i in range(start_index, end_index):
                line = f'{i+1}. {files[i]}'
                if len(line) > term.width:
                    # If the line is longer than the terminal width, truncate it and add ellipsis
                    line = line[:term.width - 3] + '…'
                if i == index:
                    output += term.reverse(line) + '\n'
                else:
                    output += line + '\n'

            # Fill the remaining space at the bottom
            output += '\n' * (term.height - len(output.split('\n')) - 1)

            # Print the file list
            print(output, end='', flush=True)

            with term.cbreak():
                key = term.inkey()

            if key.name == 'KEY_DOWN':
                index = min(index + 1, len(files) - 1)
            elif key.name == 'KEY_UP':
                index = max(index - 1, 0)
            elif key == '\n':
                open_file(os.path.join(directory, files[index]))

if __name__ == "__main__":
    main()
