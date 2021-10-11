import os
import requests
from zipfile import ZipFile
crash = 0
example_package = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/example.lxpkg?raw=true'
example_package_r = requests.get(example_package, allow_redirects=True)
compiler_package = 'https://github.com/Lightspace-Official/lightX-DevBox/blob/packages/compiler.lxpkg?raw=true'
compiler_package_r = requests.get(compiler_package, allow_redirects=True)
while (crash == 0):   
    text = input('lx >')

    if text == ('example'):
     print('Welcome to lightX DevBox')
    elif text == ('mk program'):
        print('Using IDE to make a new program...')
        os.system("ide.py");
    elif text == ('pkg program'):
        print('Directing you to packager...')
        os.system("Package.py");
    elif text == ('run program'):
        print('Which program? (Input relative path)')
        program_run = input('')
        os.system('python ' + program_run);
    elif text == ('unpkg program'):
        print('Directing you to unpackager...')
        os.system('Unpackage.py');
    elif text == ('install pkg'):
        progam_to_be_installed = input('Which program?')

        if progam_to_be_installed == ('example'):
            open('example.lxpkg', 'wb').write(example_package_r.content)
            file_name = ('example.lxpkg')
            with ZipFile(file_name, 'r') as zip:
  
            # extracting all the files
             print('Installing example...')
             zip.extractall()
             print('example Installed')
             print('Use cd example + run program to start example.')

        elif progam_to_be_installed == ('compiler'):
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

    elif text == ('cd'):
        cd = input('Which folder? ')
        os.chdir(cd)
        print('Changed to ' + cd)
    else:
        print('Error - Invalid command')
    
    
     
    
