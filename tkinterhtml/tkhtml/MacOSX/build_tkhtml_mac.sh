#!/usr/bin/env bash


git clone https://github.com/olebole/tkhtml3.git

cd tkhtml3

TCL=/Library/Frameworks/Tcl.framework/Versions/8.6/

# Generate some source files (see readme in https://github.com/starseeker/tcltk/tree/master/tkhtml)
tclsh src/cssprop.tcl
tclsh src/tokenlist.txt
tclsh src/mkdefaultstyle.tcl > htmldefaultstyle.c

# copy these generated files to src
mv *.c src
mv *.h src

mkdir build
cd build

# configure, make and install
chmod 755 ../configure
../configure #\
	#--prefix=$PREFIX \
	#--with-tcl=$PREFIX/lib \
	#--with-tk=$PREFIX/lib \
	#--with-tclinclude=$PREFIX/include \
	#--with-tkinclude=$PREFIX/include

make


