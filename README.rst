Wrapper for Tkhtml (http://tkhtml.tcl.tk/)

Building Tkhtml on Windows
--------------------------
In Msys run following commands

.. sourcecode:: bash

    # Generate some source files (see readme in https://github.com/starseeker/tcltk/tree/master/tkhtml)
    tclsh src/cssprop.tcl
    tclsh src/tokenlist.txt
    tclsh src/mkdefaultstyle.tcl > htmldefaultstyle.c
    
    # copy these generated files to src
    mv *.c src
    mv *.h src
    
    # create build dir
    mkdir build
    cd build
    
    TCL=/c/Tcl
    
    ../configure CFLAGS="-static-libgcc" \
        --with-tcl=$TCL/lib \
        --with-tk=$TCL/lib \
        --with-tclinclude=$TCL/include \
        --with-tkinclude=$TCL/include
    
    make    

This should result with *Tkhtml30.dll* and *pkgIndex.tcl* in *build*.

Create folder *Tkhtml* under *C:\Python35\Tcl* and copy these two files there. Add also *libgcc_s_dw2-1.dll* from MinGW bin directory.  