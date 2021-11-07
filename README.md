# lightX DevBox
A Development environment for packaging and managing lX code. Currently in its early releases, we recommend to not install lX until we launch v2.0, as some things are broken.
## How to use (for v1)
1. Install [Python 3.9](https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe) (Do not use Python 3.10)
2. Install the setup file from our releases page. (Look on the right)
3. Launch lightX from the start menu!

## New features & Notices
### New LASM Asssembly Support
lightX DB now supports LASM! (LightX Assembler) This Assembler develops for the LightX Operating System and has the feature to create new Assembly OS's. Even though this feature is still in BETA, it will be released in v2.0. This will be published in a external GLIP package.
### Modifying Main LightX DB Support
V2.0 will support external installed GLIP packages to modify the main lightX program to make new commands to the main Terminal. This enables external package makers to make usage of their package easier. 
## How to code in lX
Initilize a new project by typing 'mk program' in the lX command prompt, and after use the IDE to create your program. (lX uses python for coding, so search up for example 
python projects online.) To get started, just type 'print('Hello World!')' (without the quotes) in the IDE, click Save As, and save it in the same directory as lightX. Go back to lX Cmd Prompt, and type in 'run program', type in the full name of your program, and lX will run it for you. When you are done, use 'pkg program' to locate the folder of your project and convert it to a single lX Package. Easy as that! To unpack a code pack, use Unpackage.py manually to unpack it. For more info, visit our wiki.

## Install external packages
GLIP is the official package manager for lightX DB. GLIP stands for 'General LightX Installer Package'. You can use external packages to make your own code, such as modules and etc. To install a package, use 'install pkg' to choose a package and use it, currently only the 'example' package is available and you can download it using 'install pkg' and then 'example' to download it, then use cd to mount the 'cd' dir, and then use 'run program' and then 'example.lxp'. Well done, you have installed a external module! <br>

You can download more GLIP packages by looking and searching for what package you need. For the packages list, see our wiki.

## Build support
lX can build for Windows, but it is still in BETA, you can build by first opening lightX DB Terminal, then type 'install pkg' then 'compiler' and the wait for it to complete, then 'cd' then 'compiler' after 'run program' and then 'lx requirementsments.txt', this command will download and install all the pip packages you need for the compiler.After, 'run program', and lastly, type 'run.lxp'. This will open our GUI compiler, which you can use to compile .lxp programs.

### Use Windows CMD 
To use this you must edit the PATH so it directs you to the root directory of lightX, you can do this by opening the app called 'Edit system varibles', on this page click Path then Edit, then press 'new' and enter the directory of lightX, which usually is 'C:\Program Files (x86)\lightX DevBox'. Now you can type 'lightX' in the CMD to launch lightX!

### LASM Support
lightX DevBox supports LASM (lightX Assembler) to make and build .asm files. Use this feature by installing the module called `lasm` and this will modify the main lightX code to build .asm files.

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
- [ ] Will support more programmming languages (See milestones)
- [x] Use a portable version of python to run this independently 
- [x] Make a building tool to build lX Code (See milestones)
- [x] Compile all this code 
- [x] Make support for Windows CMD 
- [x] Make support for LightX OS System & Apps
- [ ] Make support for NodeJS

## Developing a new module or package
To make a new module or package, use either compiled (.exe) or LXP programs for your module. To make a new module that makes a new command for lightX DB, make a program that modifies the main lightX DB and make a new command. 
