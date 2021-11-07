import os
import requests
from zipfile import ZipFile
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

crash = 0 # Crash variable, this causes the lightX DB to crash
# Below this comment is the package list for GLIP
example_package = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/example.lxpkg?raw=true' # Example package link
example_package_r = requests.get(example_package, allow_redirects=True)
compiler_package = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/compiler.lxpkg?raw=true' # Compiler Package link
compiler_package_r = requests.get(compiler_package, allow_redirects=True)
# Above this comment is the package list for GLIP
print('lightX DevBox Shell By Lightspace Org, Fully Open Source ') # Intro 
while (crash == 0):   
    text = input('lx >')

    if text == ('example'): # Example command
     print('Welcome to lightX DevBox')
     
    elif text == ('mk program'): # Opens the IDE to make a new program
        print('Using IDE to make a new program...')
        os.system("WPy32-3950\python-3.9.5\python.exe ide.py");

    elif text == ('pkg program'): # Packages a program folder
        print('Directing you to packager...')
        os.system("WPy32-3950\python-3.9.5\python.exe Package.py");

    elif text == ('run program'): # Runs a .lxp program
        print('Which program? (Input relative path)')
        program_run = input('')
        os.system('WPy32-3950\python-3.9.5\python.exe ' + program_run);

    elif text == ('unpkg program'): #Unpackages a lxpkg file
        print('Directing you to unpackager...')
        os.system('WPy32-3950\python-3.9.5\python.exe Unpackage.py');

    elif text == ('glip install'): # This command is used to install a package from lXPI
        progam_to_be_installed = input('Which program?')

        if progam_to_be_installed == ('example'): #example pkg install command
            open('example.lxpkg', 'wb').write(example_package_r.content)
            file_name = ('example.lxpkg')
            with ZipFile(file_name, 'r') as zip:
  
            # extracting all the files
             print('Installing example...')
             zip.extractall()
             print('example Installed')
             print('Use cd example + run program to start example.')

        elif progam_to_be_installed == ('compiler'): # compiler 'if' command
            open('compiler.lxpkg', 'wb').write(compiler_package_r.content)
            file_name2 = ('compiler.lxpkg')
            with ZipFile(file_name2, 'r') as zip:
  
            # extracting all the files
             print('Installing compiler...')
             zip.extractall()
             print('compiler Installed')
             print("Use 'cd' + 'compiler' + 'run program' + 'run.lxp' to start the compiler.")
        else:
            print('Package not found.')

    elif text == ('cd'): #cd command
        cd = input('Which folder? ')
        os.chdir(cd)
        print('Directory changed to ' + cd)

    elif text == ('lx pip install'): #This command uses PyPI to install external pip packages
        pipPackage = input('Which pip module would you like to install? ')
        os.system('pip install ' + pipPackage)
        print('All Done!')

    elif text == ('lx requirements.txt'): #This command downloads and installs all the requirements that a lX program needs
        os.system('WPy32-3950\python-3.9.5\python.exe pip install -r requirements.txt')
        print('Pip packages installed!')

    elif text == ('exit'): #Exit command
        exit()
    elif text == ('help'): # Help command
        help = input('Which command do you need help with?')
        if help == ('mk program'):
            print('This program opens the lX IDE for you to make a new program. (Though this IDE will be removed in the future)')
        elif help == ('pkg program'):
            print('This command opens the Unpackager which allows you to unpkg a .lxpkg file.')
        elif help == ('glip install'):
            print('GLIP is the default package manager of lightX DB, install packages by this command.')
        elif help == ('lx pip install'):
            print('This command installs external PyPI packages. ')
        else:
            print('Help for this command is not found')   
    else:
        print('Error - Invalid command') # Error message
    
    
     
    
