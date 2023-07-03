import os
import requests
from zipfile import ZipFile
from tkinter.filedialog import askopenfilename

crash = 0  # Crash variable, this causes the lightX DB to crash

# Package URLs for GLIP
example_package_url = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/example.lxpkg?raw=true'
compiler_package_url = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/compiler.lxpkg?raw=true'
nasm_package_url = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/nasm.lxpkg?raw=true'
nodejs_package_url = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/nodejs.lxpkg?raw=true'


# Fetching package files
example_package_r = requests.get(example_package_url, allow_redirects=True)
compiler_package_r = requests.get(compiler_package_url, allow_redirects=True)

print('lightX DevBox Shell By Lightspace Org, Fully Open Source')  # Intro

while crash == 0:
    text = input('lx > ')

    if text == 'example':
        print('Welcome to lightX DevBox')

    elif text == 'mk program':
        print('Using IDE to make a new program...')
        os.system("WPy32-3950\python-3.9.5\python.exe ide.py")

    elif text == 'pkg program':
        print('Directing you to packager...')
        os.system("WPy32-3950\python-3.9.5\python.exe Package.py")
    
    elif text.startswith('run '):
        program_run = text[4:]
        os.system(r'WPy32-3950\python-3.9.5\python.exe ' + program_run + r'\run.lxp')

    elif text.startswith('runw '):
        program_run = text[5:]
        os.system(r'start ' + program_run + r'\run.exe')
        
    elif text == 'unpkg program':
        print('Directing you to unpackager...')
        os.system('WPy32-3950\python-3.9.5\python.exe Unpackage.py')

    elif text.startswith('glip install '):    
        program_to_be_installed = text[13:]
        package_url = (r'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/' + program_to_be_installed + r'.lxpkg?raw=true')
        package_r = requests.get(package_url, allow_redirects=True)
        open(program_to_be_installed + r'.lxpkg', 'wb').write(package_r.content)
        file_name2 = program_to_be_installed + r'.lxpkg'
        with ZipFile(file_name2, 'r') as zip_file:
            print(r'Installing ' + program_to_be_installed)
            zip_file.extractall()
            print(program_to_be_installed + r' installed')
            print(r'Use run or runw (for .exe apps)' + program_to_be_installed + r' to run the program')

    elif text.startswith('cd '):
        cd = text[3:]  # Extract folder name from command
        os.chdir(cd)
        print('Directory changed to ' + cd)

    elif text.startswith('lx pip install '):
        pip_package = text[16:]  # Extract package name from command
        os.system('pip install ' + pip_package)
        print('Installation complete!')

    elif text == 'lx requirements.txt':
        os.system('\WPy32-3950\WinPython%20Command%20Prompt.exe pip install -r requirements.txt')
        print('Pip packages installed!')

    elif text == 'ls':
        files = os.listdir()
        for file in files:
            print(file)

    elif text.startswith('cat '):
        file_name = text[4:]  # Extract file name from command
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print('File not found!')

    elif text == 'exit':
        exit()

    elif text == 'help':
        print('Available commands:')
        print('example                 - Welcome message')
        print('mk program              - Open the IDE to make a new program')
        print('pkg program             - Package a program folder')
        print('run program             - Run a .lxp program')
        print('unpkg program           - Unpackage a .lxpkg file')
        print('glip install            - Install a package from lXPI')
        print('cd <folder>             - Change directory')
        print('lx pip install <module> - Install external PyPI packages')
        print('lx requirements.txt     - Install required packages from requirements.txt')
        print('ls                      - List files in the current directory')
        print('cat <file>              - Display the content of a file')
        print('exit                    - Exit the program')
        print('help                    - Display this message')

    else:
        print('Error - Invalid command')  # Error message for invalid command
    
