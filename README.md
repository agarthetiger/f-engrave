# F-Engrave

Run F-Engrave on MacOS from the command line. This fork exists to eliminate insecure practices like disabling [SIP](https://support.apple.com/en-gb/HT204899) which is unnecessary. Tested on Catalina.


## Prerequisites

The following software must be present.
`g++` - Provided by XCode Developer Tools


## Compiling

In the main directory run `build.sh`.  This will create a clickable OSX Application in the ./dist directory named `f-engrave.app` that can then be distributed or moved to your Applications folder.

There are a few complications with compilation that are not addressed in the macOS `build.sh` script and need to be handled manually before compiling. These stem from the System Integrity Protection on macOS (since 10.10) and the system Python packager, `py2app`.


## Dependencies

* `g++`
* `XQuartz` (for `libfreetype2`)

The application builds and includes `ttf2cxf` (modified makefile for a macOS system with X11 in `/usr/X11`) to allow engraving of TrueType (`ttf`) fonts. This adds the requirement for `XQuartz` and it's provided library `libfreetype2` installed to compile.

For True Type fonts to be read by F-engrave the ttf2cxf_stream program needs to be compiled and placed in the system path.

F-Engrave will function properly without the ttf2cxf executable but it will not show or read .ttf files.

The application does not include `potrace`. If `potrace` is installed in the system path or in `/usr/local/bin` (e.g. Homebrew) then bitmap (`PBM`) files can be read and utilized.


* `TTF2CXF_STREAM/Makefile` has a target added to compile it on macOS. 

##  About F-Engrave

F-Engrave generates 'GCODE' for Computer Numerical Control (CNC) systems from text and bitmaps. It "Suppoprts Engraving and V-Carving, Uses CXF and TTF fonts, Imports DXF and Bitmap images".

The official F-Engrave and instructions are at the official [Scorchworks F-Engrave website][fengrave]
