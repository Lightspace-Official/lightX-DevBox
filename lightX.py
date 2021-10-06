import os

crash = 0
while (crash == 0):   
    text = input('lx >')

    if text == ('example'):
     print('Welcome to lightX DevBox')
    elif text == ('mk program'):
        print('Using IDE to make a new program...')
        os.system("ide.py");
        raw_input();
    elif text == ('pkg program'):
        print('Directing you to packager...')
        os.system("Package.py");
        raw_input();
    elif text == ('run program'):
        print('Which program? (Input relative path)')
        program_run = input('')
        os.system(program_run);
        raw_input();
    else:
        print('Error - Invalid command')
    
    
     
    
