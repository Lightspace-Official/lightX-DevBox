# lightX DevBox
A Development environment for packaging and managing lX code. Currently in very early BETA.
## How to use
1. Download the zip file from here.
2. Extract it somewhere, easily accessible.
3. Download Python 3.
4. Run lightX.py

## How to code in lX
Initilize a new project by typing 'mk program' in the lX command prompt, and after use the IDE to create your program. (lX uses python for coding, so search up for example 
python projects online.) To get started, just type 'print('Hello World!')' (without the quotes) in the IDE, click Save As, and save it in the same directory as lightX. Go back to lX Cmd Prompt, and type in 'run program', type in the full name of your program, and lX will run it for you. When you are done, use 'pkg program' to locate the folder of your project and convert it to a single lX Package. Easy as that! To unpack a code pack, use Unpackage.py manually to unpack it.

## Install external packages
lX can install external packages and apps from our repo so you can use external code to make your own, such as mosules and etc. To install a package, use 'install pkg' to choose a package and use it, currently only the 'example' package is available and you can download it using 'install pkg' and then 'example' to download it, then use cd to mount the 'cd' dir, and then use 'run program' and then 'example.lxp'. Well done, you have installed a external module!

## Commands 
* mk program
* run program
* package program 
* example
* install pkg

## Roadmap
- [ ] Will support more programmming languages 
- [ ] Use a portable version of python to run this independently 
- [ ] Make a building tool to build lX Code (See milestones)
- [ ] Compile all this code 
- [ ] Make support for Windows CMD
- [ ] Make build support 
