# lightX DevBox
A Development environment for packaging and managing lX code. Currently in very early BETA.
## How to use
1. Install the latest release, by the setup .exe.
2. launch lightX
3. You're done!

## How to code in lX
Initilize a new project by typing 'mk program' in the lX command prompt, and after use the IDE to create your program. (lX uses python for coding, so search up for example 
python projects online.) To get started, just type 'print('Hello World!')' (without the quotes) in the IDE, click Save As, and save it in the same directory as lightX. Go back to lX Cmd Prompt, and type in 'run program', type in the full name of your program, and lX will run it for you. When you are done, use 'pkg program' to locate the folder of your project and convert it to a single lX Package. Easy as that! To unpack a code pack, use Unpackage.py manually to unpack it.

## Install external packages
lX can install external packages and apps from our repo so you can use external code to make your own, such as mosules and etc. To install a package, use 'install pkg' to choose a package and use it, currently only the 'example' package is available and you can download it using 'install pkg' and then 'example' to download it, then use cd to mount the 'cd' dir, and then use 'run program' and then 'example.lxp'. Well done, you have installed a external module!

## Build support
lX can build for Windows, but it is still in BETA, you can build by first using (Use lightX to do this), 'install pkg' then 'compiler' and the wait for it to complete, then 'cd' then 'compiler' after 'run program' and then 'lx requirementsments.txt', this command will download and install all the pip packages you need for the compiler.After, 'run program', and lastly, type 'run.lxp'. This will open our GUI compiler, which you can use to compile .lxp programs.

### Use Windows CMD 
To use this you must edit the PATH so it directs you to the root directory of lightX, you can do this by opening the app called 'edit system varibles' on this page click Path then Edit, then press 'new' and enter the directory of lightX, which normally is 'C:\Program Files (x86)\lightX DevBox'.Now you can type 'lightX' in the CMD to launch lightX!

## Commands 
* mk program - Opens the IDE for you to make a new lxp program
* run program - Runs a lxp program
* pkg program - Packages a program folder and all the programs inside it
* example - A example command
* install pkg - Installs a external package from the lX server
* cd - Mounts a directory
* lx pip - Installs a external PyPI package for lxp programs
* lx requirements.txt - Installs all the PyPI packages needed for a program

## Roadmap
- [ ] Will support more programmming languages 
- [ ] Use a portable version of python to run this independently 
- [x] Make a building tool to build lX Code (See milestones)
- [ ] Compile all this code 
- [x] Make support for Windows CMD
- [ ] Make build support 
